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
PDF_DIR = 'pdf_input'
JS_START = r'// [template start]'
JS_END = r'// [template end]'
CODE_LEN = 256
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
        self.cur_file = ''
        if not os.path.exists(TEST_DIR):
            os.mkdir(TEST_DIR)

    def zip_file(self, count):
        cmd = r'"C:\Program Files\7-Zip\7z.exe" a db/cov%d cov' % count
        p = subprocess.Popen(cmd)
        p.wait()
        for i in os.listdir('cov'):
            fpath = os.path.join('cov', i)
            if os.path.exists(fpath):
                os.remove(fpath)

    def runPDF(self):
        count = 0
        flst = os.listdir(TEST_DIR)
        i = 0
        for fname in flst:
        #fpath = os.path.join(TEST_DIR, fname)
        #print("find file %s" % fpath)
            m = monitor.Monitor(fname)
            m.startUp()
            if (i+1) % 100 == 0:
                self.zip_file(count)
                count += 1
            i += 1

'''
        for i in range(TEST_NUM):
            self.new_test()
            m = monitor.Monitor(self.cur_file+'.pdf')
            m.startUp()
            if (i+1) % 100 == 0:
                self.zip_file(count)
                count += 1
            # m.writeResult()
'''

if __name__ == '__main__':
    if not os.path.exists('cov'):
        os.makedirs('cov')
    if not os.path.exists('db'):
        os.makedirs('db')
    f = JSFuzz()
    f.runPDF()
