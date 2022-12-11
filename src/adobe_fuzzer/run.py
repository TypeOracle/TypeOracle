import generate
import mPDF
import os
import monitor

TESTDIR = 'test'
SNUM = 256
TNUM = 200000

def getname(elem):
    ret = 0
    try:
        ret = int(elem.split(".")[0])
    except Exception as e:
        print(str(e))
    return ret
    
class JSFuzz:

    def __init__(self):
        self.gen = generate.Generator()
        if not os.path.exists(TESTDIR):
            os.makedirs(TESTDIR)
        self.ind = 0
        self.curfname = ''

    def new_test(self):
        self.gen.clean_status()
        tmp = self.gen.create(SNUM)
        tmp = 'try{spell.available}catch(e){};\n'+tmp+'\ncloseDoc(1);\n'
        fpath = os.path.join(TESTDIR, '%d.pdf' % self.ind)
        self.curfname = '%d.pdf' % self.ind
        self.ind += 1
        mPDF.make_pdf(tmp, fpath)

    def run_testcase(self):
        m = monitor.Monitor(self.curfname)
        m.startUp()
        m.writeResult()

    def startup(self):
        for _ in range(TNUM):
            self.new_test()
            print(self.curfname)
            try:
                self.run_testcase()
            except Exception as e:
                pass


if __name__ == '__main__':
    f = JSFuzz()
    f.startup()
