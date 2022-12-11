import random

def P(p):
    return random.randint(0, 99) < p

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