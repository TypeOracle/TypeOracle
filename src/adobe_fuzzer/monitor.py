# coding=utf-8
import os
import sys
import time
import subprocess
import psutil
import pywinauto
import win32api

ADOBE_PATH = r'C:\"Program Files (x86)"\Adobe\"Acrobat Reader DC"\Reader\AcroRd32.exe'

TEST_DIR = os.path.join(os.getcwd(),'test')


class Monitor:

    def __init__(self, fileName, timeOut=120):
        self.status = 'init'
        self.fileName = fileName
        self.timeOut = timeOut
        self.crash_key = ''

    def log(self, info):
        # %Y-%m-%d
        t = time.strftime("%H:%M:%S", time.localtime())
        print(t + ' ' + info)

    def getPidsByName(self, pname):
        return [p.info['pid']
                for p in psutil.process_iter(attrs=['pid', 'name'])
                if p.info['name'] == pname]

    def closeProcess(self, pname):
        try:
            list_ = [psutil.Process(i)
                 for i in self.getPidsByName(pname)]
            for p in list_:
                if p.is_running():
                    p.kill()
        except Exception as e:
            self.log(e)

    # def run_windbg(self):
    #     cmd = '%s %s' % (ADOBE_PATH, os.path.join(CUR_PATH, 'test.pdf'))
    #     print(cmd)

    #     subprocess.Popen(cmd, shell=True)
    #     time.sleep(5)

    #     pid = self.getPidsByName('AcroRd32.exe')[0]
    #     self.pid = pid
    #     self.log('checkStart - pid:%d' % self.pid)

    #     cmd = 'cd %s&windbg.exe -p %d -c ".load pykd;!py -g %s"' % (
    #         WINDBG_PATH, pid, os.path.join(CUR_PATH, 'record.py')
    #     )
    #     print(cmd)

    #     subprocess.Popen(cmd, shell=True)
    #     time.sleep(5)

    #     self.app = pywinauto.Application().connect(process=self.pid)
    #     self.status = 'running'

    def clearDerived(self):
        list_ = ['AcroRd32.exe', 'AdobeCollabSync.exe', 'AdobeARM.exe',
                 'RdrCEF.exe', 'WerFault.exe', 'splwow64.exe']
        for i in list_:
            self.closeProcess(i)

    def checkStart(self):
        pid_lst = self.getPidsByName('AcroRd32.exe')
        if len(pid_lst) > 0:
            self.pid = pid_lst[0]
            self.app = pywinauto.Application().connect(process=self.pid)
            self.status = 'running'
            self.log('checkStart - pid:%d' % self.pid)
            return 1
        return 0

    def openPDF(self):
        self.popup = 0
        fpath = os.path.join(TEST_DIR, self.fileName) if len(
            TEST_DIR) > 0 else self.fileName
        cmd = '%s %s'%(ADOBE_PATH,fpath)
        print(cmd)
        subprocess.Popen(cmd,shell=True)
        #win32api.ShellExecute(0, 'open', fpath, '', '', 1)
        ret = 0
        for _ in range(10):
            time.sleep(1)
            if self.checkStart():
                ret = 1
                break
        return ret == 1

    def checkHalt(self):
        ret = 0
        if not self.app.is_process_running():
            ret = 1
            self.status = 'halt'
            self.log('Check - Halt')
        return ret

    def checkCrash(self):
        ret = 0
        list_ = self.getPidsByName('WerFault.exe')
        if len(list_) > 0:      

            ret = 1
            self.status = 'crash'
            self.log('Check - crash')
            self.closeProcess('WerFault.exe')
            if self.app.is_process_running():
                self.app.kill()
        return ret

    def checkPop(self):

        try:
            ret = 1
            self.closeProcess("VMwareHostOpen.exe")


            for win in self.app.windows():
                if win.class_name() == 'AcrobatSDIWindow':
                    win.set_focus()
                    break

            win = self.app.top_window()
            cname = win.class_name()
            # self.log(cname)
            if cname != 'AcrobatSDIWindow':
                win.set_focus()
                self.log(cname)
                if cname == '#32768':
                    pywinauto.keyboard.send_keys('%{a}')
                    # 只要alt就行 但可能导致选择到菜单 导致下个文档无法正常打开
                else:
                    pywinauto.keyboard.send_keys('%{F4}')
                self.popup = 1
            elif win.window_text().startswith('Adobe Acrobat Reader DC'):
                self.status = 'finish'
                self.log('Check - close')
                try:
                    win.close()
                except Exception as e:
                    pass
            else:
                # self.log(cname)
                # pywinauto.keyboard.send_keys('%')
                ret = 0
        except Exception as e:
            self.log(str(e))
            self.popup = 1
            ret = 1

        return ret

    def checkStatus(self, enter=0):
        if psutil.cpu_percent(interval=1.0) < 20:
            if not self.checkHalt():
                if not self.checkCrash():
                    if not self.checkPop():
                        if enter:
                            self.status = 'stop'
                            self.log('Check - stop')
                        else:
                            self.log('Check - low cpu usage')
                            time.sleep(2)
                            self.checkStatus(1)

    def checkMain(self):
        startTime = time.time()
        ret = 0

        for _ in range(self.timeOut // 2):
            time.sleep(1)
            self.checkStatus()
            if self.status != 'running':
                ret = 1
                break

        if not ret:
            self.status = 'hang'
            self.log('Check - hang')

        runTime = int(time.time() - startTime)
        self.log('End - running time: ' + str(runTime))

    def writeResult(self):
        with open('runlog.txt', 'a') as f:
            f.write('%d %s %s %s %s\n' %
                    (int(time.time()), self.fileName, self.status, str(self.popup), self.crash_key))
        return self.status

    def closeReader(self):
        if self.status == 'finish':
            for _ in range(10):
                time.sleep(1)
                if (not self.app.is_process_running()) or \
                        self.checkCrash():
                    break
        if self.app.is_process_running():
            self.app.kill()

    def savePDF(self):
        if self.status != 'finish':
            if not os.path.exists('save'):
                os.makedirs('save')

            spath = os.path.join('save', self.status)
            if not os.path.exists(spath):
                os.makedirs(spath)            
            

            newpath = os.path.join(spath, self.fileName)
            oripath = os.path.join(TEST_DIR, self.fileName) \
                if len(TEST_DIR) > 0 else self.fileName

            with open(oripath, 'rb') as f:
                data = f.read()
            with open(newpath, 'wb') as f:
                f.write(data)

            self.log('Save - %s - %s' % (self.status, self.fileName))

    def startUp(self):
        try:
            if self.openPDF():
                self.checkMain()
                self.closeReader()
        except Exception as e:
            self.status = 'error'
            self.log(str(e))

        self.clearDerived()
        self.savePDF()
        # self.writeResult()

        # return self.status


if __name__ == '__main__':
    m = Monitor("5048.pdf")
    m.startUp()
    # tmp = os.listdir('test')
    # tmp.sort()
    # flag = 0
    # for fname in tmp:
    #     # if flag == 0:
    #     #     if fname == 'this_getUserUnitSize.pdf':
    #     #         flag = 1
    #     #     else:
    #     #         continue
    #     print(fname)
    #     m = Monitor(fname)
    #     m.startUp()
    # # m.writeResult()
