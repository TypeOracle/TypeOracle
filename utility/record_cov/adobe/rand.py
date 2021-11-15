import os
import random


def rand_integer():
    flag = random.randint(0, 10)
    if flag > 5:  # 5/11
        r = random.randint(0x0, 0xf)
    elif flag > 2:  # 3/11
        r = random.randint(0xf, 0xfff)
    elif flag > 0:  # 2/11
        r = random.randint(0xfff, 0xffff)
    else:  # 1/11
        r = random.randint(0xffff, 0x80000000)
    return str(r)


def rand_ascii(if_arr):
    def m1():
        a = random.randint(0x41, 0x5a)
        b = random.randint(0x61, 0x7a)
        return random.choice([a, b])

    def m2():
        return random.randint(0x20, 0x7e)

    def m3():
        return random.randint(0x0, 0xff)

    def choose():
        flg = random.randint(0, 2)
        if flg == 0:
            r = m1()
        elif flg == 1:
            r = m2()
        else:
            r = m3()
        return '\\\\x' + hex(r + 0x100)[3:]

    def level():
        if random.choice([0, 1]):
            r = random.randint(0x1000, 0x10000)
        else:
            r = random.randint(0x10, 0x1000)
        return '0x' + hex(r)[2:]

    if if_arr:
        return 'Array(%s).join("%s")' % (level(), choose())
    else:
        len_ = int(random.normalvariate(5, 5))
        if len_ < 0:
            len_ *= -1
        arr = [choose() for _ in range(len_)]
        return '"%s"' % ''.join(arr)


# pure unicode string
def rand_unicode(if_arr):
    def choose():
        return '\\\\u' + hex(random.randint(0x0, 0xffff) + 0x10000)[3:]

    def level():
        if random.choice([0, 1]):
            r = random.randint(0x1000, 0x8000)
        else:
            r = random.randint(0x10, 0x1000)
        return '0x' + hex(r)[2:]

    if if_arr:
        return 'Array(%s).join("%s")' % (level(), choose())
    else:
        len_ = int(random.normalvariate(5, 5))
        if len_ < 0:
            len_ *= -1
        arr = [choose() for _ in range(len_)]
        return '"%s"' % ''.join(arr)


class Constant:

    def __init__(self):
        self.dic = {'0': self.rand_bool,
                    '1': self.rand_num,
                    '2': self.rand_obj,
                    '3': self.rand_str}
        fpath = os.path.join('config', 'constant.txt')
        with open(fpath, 'r') as f:
            raw = f.read()
        self.objlst = [i for i in raw.split('\n') if len(i) > 0]

    def dispatcher(self, typeid):
        if typeid in self.dic:
            func = self.dic[typeid]
            return func()
        else:
            keylst = list(self.dic.keys())
            return self.dispatcher(random.choice(keylst))

    def rand_bool(self):
        return random.choice(['true', 'false'])

    def rand_num(self):
        c = '' if random.randint(1, 5) != 1 else '-'
        return '%s%s.%s' % (c, rand_integer(), ''.join(reversed(rand_integer())))

    def rand_str(self):
        tmp = random.randint(0, 9)
        if tmp > 5:
            return rand_ascii(0)
        elif tmp > 2:
            return rand_ascii(1)
        elif tmp > 0:
            return rand_unicode(0)
        else:
            return rand_unicode(1)

    def rand_obj(self):
        tmp = random.choice([0,1])
        if tmp == 0:
            return r'{}'
        else:
            return r'[]'
        # else:
        #     return random.choice(self.objlst)


if __name__ == '__main__':
    c = Constant()
    lst = ['0', '1', '2', '3']
    for i in lst:
        tmp = c.dispatcher(i)
        print(tmp)
