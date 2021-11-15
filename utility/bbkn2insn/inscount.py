import os
import struct
import idc
import idaapi

INPUT_DIR = 'adobe_sample_input'
OUTPUT_DIR = 'adobe_sample_output'
CUR_PATH = r'C:\Users\wxy\TyFuzzer\exp2\bbkn2insn'

def get_bbk_ins(addr, sizet):
    count = 1
    cursize = idc.ItemSize(addr)
    maxcount = 100
    while cursize < sizet:
        curaddr = addr+cursize
        count += 1
        cursize += idc.ItemSize(curaddr)
        if count > maxcount:
            break
    return count


def load_file(fpath):
    with open(fpath, 'rb') as f:
        raw = f.read()
    count = int(len(raw)/6)
    tmp = []
    for i in range(count):
        bt = raw[6*i:6*i+6]
        offset, sizet = struct.unpack('<IH', bt)
        tmp.append((offset, sizet))
    return tmp


def encode_data(offset_, size_):
    return str(offset_)+'_'+str(size_)


def decode_data(st):
    a, b = st.split('_')
    return int(a), int(b)


def update_bbk(fpath, curbbk):
    bbklst = set([encode_data(i[0], i[1]) for i in load_file(fpath)])
    updatelst = [decode_data(i) for i in bbklst-curbbk]
    return bbklst | curbbk, updatelst


def count_ins(tmplst, imgbase):
    count = 0
    for ind, item in enumerate(tmplst):
        if (ind+1) % 1000 == 0:
            print('%d/%d' % (ind+1, len(tmplst)))
        offset, sizet = item
        r = get_bbk_ins(offset+imgbase, sizet)
        count += r
    return count


def main():
    idc.Wait()

    imgbase = idaapi.get_imagebase()
    tmp = idc.get_input_file_path()
    curfname = tmp.split('\\')[-1]

    res = []

    sizecount = 0
    curbbk = set([])

    respath = os.path.join(CUR_PATH,INPUT_DIR)

    flst = os.listdir(respath)
    for i in range(len(flst)):
        f1 = os.path.join(respath, str(i))
        f2 = os.path.join(f1, curfname)
        if not os.path.exists(f2):
            print(f2+' not found')
            res.append('%d,%d' % (i, sizecount))
            continue
        print(f2)
        ncurbbk, newbbk = update_bbk(f2, curbbk)
        curbbk = ncurbbk
        newcount = count_ins(newbbk,imgbase)
        sizecount += newcount
        res.append('%d,%d' % (i, sizecount))
        print('[+] newcount/totalcount : %d/%d' % (newcount, sizecount))

    nfname = 'log-'+'_'.join(curfname.split('.'))+'.txt'
    datapath = os.path.join(CUR_PATH, OUTPUT_DIR)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(os.path.join(datapath, nfname), 'w') as f:
        f.write('\n'.join(res))

    idc.Exit(0)


if __name__ == '__main__':
    main()


# fpath = os.path.join('coverage', 'EScript.api')
# tmp = load_file(fpath)
# print('total: ', len(tmp))
# count = 0
# for ind, item in enumerate(tmp):
#     if (ind+1) % 1000 == 0:
#         print('%d/%d' % (ind+1, len(tmp)))
#     offset, sizet = item
#     r = get_bbk_ins(offset+imgbase, sizet)
#     count += r
# print('result: ', count)
