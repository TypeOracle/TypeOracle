import os
import subprocess

IDA_PATH = r'"C:\Program Files\IDA 7.0\idat.exe"'
# CUR_PATH = r"C:\Users\wxy\Desktop\idabatch"
IDB_PATH = 'adobe_idb'

def main():

    flst = os.listdir(IDB_PATH)
    plst = [os.path.join(IDB_PATH, i) for i in flst]

    for i in plst:
        print(i)
        cmd = '%s -a -A -Sinscount.py %s' % (IDA_PATH, i)
        # print(cmd)
        p = subprocess.Popen(cmd, shell=True)
        p.wait()


if __name__ == "__main__":
    main()
