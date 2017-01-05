# -*- coding: utf-8 -*-
import optparse
from func import globalip, ProxyVerification, writeip, run, validateIP, getxiciproxyip, readline, get666ip
from multiprocessing import Pool
import threading
import time
import sys
import signal
num = 0
flage = 0
kztest=u"""

使用方法:
    "验证代理ip"
    "
    -y "要验证的文件名"
    -t "要启动的线程"
    -f "验证通过，保存文件地址"
    "

    "爬去代理ip并验证"
    "
    '-n'      "要提取IP的数量"
    '-f'      "验证完成的代理IP保存地址"
    '-j'      "当网页抓取的代理不够时，自行生成代理IP的进程数"
    '-t'      "验证代理IP启动的线程数"
    '-p'      "当网页抓取的代理不够时，自行生成代理ip要扫描的端口号"
    "

"""

def main():
    parser = optparse.OptionParser(
        u"usage%prog -n '<IP 数量>' -f '<保存的文件名>' -t '<进程数>' -p '<端口号>(用','分割)' '-j' '<随机抓取ip的进程数>'")
    parser.add_option('-n', dest="IPnum", type="string", help=u'要抓取的ip数量')
    parser.add_option('-f', dest="FileName", type="string", help=u'保存验证完成的文件名')
    parser.add_option('-j', dest="processnum", type="int",
                      help=u"随机抓取要启动的进程数(随机抓取专用)")
    parser.add_option('-t', dest="threadnum",
                      type="int", help=u"验证代理线程数量(验证专用)")
    parser.add_option('-p', dest="ports", type='string',
                      help=u"要扫描的端口号，用','分割")
    parser.add_option('-y', dest="filen", type="string", help=u"需要验证的文件名")
    (options, args) = parser.parse_args()
    """验证代理ip"""
    """
    -y "要验证的文件名"
    -t "要启动的线程"
    -f "验证通过，保存文件地址"
    """
    if options.filen != None and options.threadnum != None and options.IPnum == None and options.FileName != None and options.ports == None:
        filen = options.filen
        threadnum = options.threadnum
        FileName = options.FileName
        iplist = []
        thread_list = []
        try:
            f = open(filen, 'r')
        except IOError as e:
            print u"%s不存在，请检查输入的文件名" % (filen)
            exit(0)
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            iplist.append(line)
        f.close()
        try:
            fsave = open(FileName, 'w')
        except IOError as e:
            print u"%s文件异常" % (FileName)
            exit()
        for ip in iplist:
            t = threading.Thread(target=validateIP, args=(fsave, ip))
            thread_list.append(t)
        for t in thread_list:
            if len(threading.enumerate()) < threadnum:
                t.start()
                # print len(threading.enumerate())
            else:
                time.sleep(0.1)
        for t in thread_list:
            try:
                t.join()
            except Exception, e:
                pass
        fsave.close()
    """爬去代理ip并验证"""
    """
    '-n'      "要提取IP的数量"
    '-f'      "验证完成的代理IP保存地址"
    '-j'      "当网页抓取的代理不够时，自行生成代理IP的进程数"
    '-t'      "验证代理IP启动的线程数"
    '-p'      "当网页抓取的代理不够时，自行生成代理ip要扫描的端口号"
    """
    if options.IPnum != None and options.FileName != None and options.processnum != None and options.threadnum != None and options.ports != None and options.filen == None:
        IPnum = options.IPnum
        FileName = options.FileName
        processnum = options.processnum
        threadnum = options.threadnum
        ports = str(options.ports).split(',')
        iplist = get666ip()
        TransferIP = []
        testIP = []
        try:
            fsave = open(FileName, 'w')
        except IOError as e:
            print u"%s不存在，请检查输入的文件名" % (FileName)
            exit()
        thread_list = []
        for ip in iplist:
            t = threading.Thread(target=validateIP, args=(fsave, ip))
            thread_list.append(t)
        for t in thread_list:
            if len(threading.enumerate()) < threadnum:
                t.start()
            else:
                time.sleep(0.1)
        for t in thread_list:
            try:
                t.join()
            except Exception, e:
                pass
        fsave.close()
        """返回当前文件的行数，ip数量"""
        try:
            fsave = open(FileName, 'r')
            linenum = readline(fsave)
        except Exception:
            print u"读取文件异常"
        fsave.close()
        if int(linenum) < int(IPnum):
            thread_list = []
            iplist = getxiciproxyip()
            try:
                fsave = open(FileName, 'a')
            except IOError as e:
                print u"打开文件异常"
                exit()
            for ip in iplist:
                th = threading.Thread(target=validateIP, args=(fsave, ip))
                thread_list.append(th)
            for th in thread_list:
                if len(threading.enumerate()) < threadnum:
                    th.start()
                    # print len(threading.enumerate())
                else:
                    time.sleep(0.1)
            for th in thread_list:
                try:
                    th.join()
                except Exception, e:
                    pass
            fsave.close()
            """返回当前文件的行数，ip数量"""
            try:
                fsave = open(FileName, 'r')
                linenum = readline(fsave)
            except Exception:
                print u"读取文件异常"
            fsave.close()
            if int(linenum) < int(IPnum):
                need = (int(IPnum) - int(linenum)) * 10
                while True:
                    time.sleep(5)
                    if int(linenum) <= int(IPnum):
                        print int(linenum)<int(IPnum)
                        time.sleep(5)
                        try:
                            fsave = open(FileName, 'a')
                        except IOError as e:
                            print u"打开文件异常"
                            exit()
                        thread_list = []
                        pool = Pool(processnum)
                        for processn in range(need):
                            res = pool.apply_async(func=globalip)
                            TransferIP.append(res)
                        pool.close()
                        pool.join()
                        for res in TransferIP:
                            testIP.append(res.get())
                        for ip in testIP:
                            t = threading.Thread(
                                target=ProxyVerification, args=(fsave, ip, ports))
                            thread_list.append(t)
                        for t in thread_list:
                            if len(threading.enumerate()) < threadnum:
                                t.start()
                                # print len(threading.enumerate())
                            else:
                                time.sleep(0.1)
                        for t in thread_list:
                            try:
                                t.join()
                            except Exception, e:
                                pass
                        fsave.close()
                        try:
                            fsave = open(FileName, 'r')
                            linenum = readline(fsave)
                            print linenum
                            time.slppe(3)
                        except Exception:
                            continue
                        finally:
                            fsave.close()
                    else:
                        try:
                            fsave = open(FileName, 'r')
                            linenum = readline(fsave)
                            print "一共找到%d条可用代理!" % (linenum)
                        except Exception:
                            print u"读取文件异常"
                        finally:
                            fsave.close()
                            exit(0)

            else:
                try:
                    fsave = open(FileName, 'r')
                    linenum = readline(fsave)
                    print "一共找到%d条可用代理!" % (linenum)
                except Exception:
                    print u"读取文件异常"
                finally:
                    fsave.close()
                    exit(0)

        else:
            try:
                fsave = open(FileName, 'r')
                linenum = readline(fsave)
                print "一共找到%d条可用代理!" % (linenum)
            except Exception:
                print u"读取文件异常"
            finally:
                fsave.close()
                exit(0)

    else:
        print kztest

if __name__ == '__main__':
    main()
