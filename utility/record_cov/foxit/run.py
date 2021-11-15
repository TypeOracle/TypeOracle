import hashlib
import json
import os
import subprocess

import pattern
import rand
import monitor
import random

DATA_DIR = 'data'
CONFIG_DIR = 'config'
TEST_DIR = 'test'
JS_START = r'// [template start]'
JS_END = r'// [template end]'
CODE_LEN = 369
TEST_NUM = 10000


def read_json(file_name):
    with open(os.path.join(DATA_DIR, file_name), 'r') as f:
        return json.loads(f.read())


def read_text(file_name, strip_=True):
    with open(os.path.join(CONFIG_DIR, file_name), 'r') as f:
        raw = f.read()
    res = raw.split('\n')
    # if eliminate blank lines
    if strip_:
        res = [i.strip() for i in res if len(i.strip()) > 0]
    return res


class Generator:

    def __init__(self):
        blacklst = read_text('blacklist.txt')
        delist = read_text('delist.txt')

        c = rand.Constant()
        flst = os.listdir(DATA_DIR)
        dic = {}
        candidate = []
        for fname in flst:
            fpath = os.path.join(DATA_DIR, fname)
            with open(fpath, 'r') as f:
                d = json.loads(f.read())
            apiname = d['api']
            if apiname in blacklst:
                continue
            p = pattern.Pattern(d, c)
            if apiname in delist:
            	weight = 1
            else:
            	weight = self.weight(d)
            for _ in range(weight):
                candidate.append(apiname)
            dic[apiname] = p
        self.apidic = dic
        self.apilst = candidate

    def weight(self, dic):
        if dic['apitype'] == 1:
            return 2
        res = 1
        v = dic['info']
        for typeid in v:
            d = v[typeid]
            if 'req_type' in d:
                res += len(d['req_type'])
            if 'opt_type' in d and len(d['opt_type']) > 0:
                res += 1
        return res

    def one_line(self):
        apiname = random.choice(self.apilst)
        tmp = self.apidic[apiname]
        st = tmp.create()
        return 'try{%s}catch(e){}' % st

    def generate(self, codelen):
        arr = []
        for _ in range(codelen):
            tmp = self.one_line()
            arr.append(tmp)
        return '\n'.join(arr)


class JSFuzz:

    def __init__(self):
        lst = read_text('template.pdf', False)
        start_lst = []
        end_lst = []
        flag = 0
        for i in lst:
            if i == JS_END:
                flag += 1
            if flag == 0:
                start_lst.append(i)
            elif flag == 2:
                end_lst.append(i)
            if i == JS_START:
                flag += 1
        self.start = '\n'.join(start_lst)
        self.end = '\n'.join(end_lst)
        self.tool = Generator()
        self.cur_file = ''
        if not os.path.exists(TEST_DIR):
            os.mkdir(TEST_DIR)

    def new_test(self):
        block = self.tool.generate(CODE_LEN)
        self.cur_file = hashlib.md5(block.encode('utf-8')).hexdigest()
        full_pdf = '\n'.join([self.start, block, self.end])
        with open(os.path.join('test', self.cur_file + '.pdf'), 'w') as f_:
            f_.write(full_pdf)
        print('create ' + self.cur_file)

    def zip_file(self,count):
        cmd = r'"C:\Program Files\7-Zip\7z.exe" a db/cov%d cov'%count
        p = subprocess.Popen(cmd)
        p.wait()
        for i in os.listdir('cov'):
            fpath = os.path.join('cov',i)
            if os.path.exists(fpath):
                os.remove(fpath)

    def startup(self):
        count = 0
        for i in range(TEST_NUM):
            self.new_test()
            m = monitor.Monitor(self.cur_file+'.pdf')
            m.startUp()
            if (i+1)%100 == 0:
                self.zip_file(count)
                count+=1
            # m.writeResult()


if __name__ == '__main__':
    if not os.path.exists('cov'):
        os.makedirs('cov')
    if not os.path.exists('db'):
        os.makedirs('db')
    f = JSFuzz()
    f.startup()
