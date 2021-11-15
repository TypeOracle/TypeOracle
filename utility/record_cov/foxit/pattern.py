import os
import json
import random

import rand


class Pattern:

    def __init__(self, arg_info, generator):
        self.root = arg_info['root']
        self.info = arg_info['info']
        self.generator = generator
        self.api = arg_info['api']
        self.apitype = arg_info['apitype']
        self.info['21X'] = {'type':'5'}

    def handle_json(self, rule):
        req_key = rule['req_key']
        req_type = rule['req_type']
        opt_key = rule['opt_key']
        opt_type = rule['opt_type']

        arr = []

        for k, v in zip(req_key, req_type):
            tmp = self.dispatcher(v)
            arr.append('%s:%s' % (k, tmp))

        for k, v in zip(opt_key, opt_type):
            if random.choice([0, 1]):
                tmp = self.dispatcher(v)
                arr.append('%s:%s' % (k, tmp))

        return '{%s}' % ','.join(arr)

    def handle_arr(self, rule):
        req_type = rule['req_type']
        opt_type = rule['opt_type']

        arr = []

        for t in req_type:
            tmp = self.dispatcher(t)
            arr.append(tmp)

        for t in opt_type:
            if random.choice([0, 1]):
                tmp = self.dispatcher(t)
                arr.append(tmp)
            else:
                break

        return '[%s]' % ','.join(arr)

    def handle_conarr(self, rule):
        arrlen = random.randint(0, 7)
        curtype = rule['type']

        arr = []

        for _ in range(arrlen):
            tmp = self.dispatcher(curtype)
            arr.append(tmp)

        return '[%s]' % ','.join(arr)

    def handle_multi(self, rule):
        candidate = rule['typelist']
        curtype = random.choice(candidate)

        return self.dispatcher(curtype)

    def dispatcher(self, typeid, root=False):
        if typeid in self.info:

            if not root and typeid.startswith('2') and random.randint(0, 9) == 0:
                return self.generator.dispatcher('2')

            tmp = self.info[typeid]
            if typeid.startswith('23'):
                return self.handle_json(tmp)
            elif typeid.startswith('22'):
                return self.handle_arr(tmp)
            elif typeid.startswith('21'):
                return self.handle_conarr(tmp)
            elif typeid.startswith('5'):
                return self.handle_multi(tmp)
            else:
                return ''
        else:
            return self.generator.dispatcher(typeid)

    def create(self):
        if self.apitype == 0:
            flag = random.randint(0,10)
            if flag < 3:
                tmp = self.dispatcher('21X',True)
            else:
                tmp = self.dispatcher(self.root, True)
            if tmp[0] == '[':
                tmp = tmp[1:-1]
            return '%s(%s)' % (self.api, tmp)
        else:
            flag = random.randint(0,10)
            if flag < 3:
                tmp = self.dispatcher('5')
            else:
                tmp = self.dispatcher(self.root)
            return '%s=%s' % (self.api, tmp)


if __name__ == '__main__':
    c = rand.Constant()
    fpath = os.path.join('tmpdata','this_tts_volume.json')
    with open(fpath, 'r') as f:
        d = json.loads(f.read())
    p = Pattern(d, c)
    for _ in range(50):
        tmp = p.create()
        print(tmp)
