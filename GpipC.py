# -*- coding: utf-8 -*-
import optparse
from func import globalip,getip,ProxyVerification,writeip,run,getnum,validateIP
from multiprocessing import Pool
import threading
import time
iplist = []
num = 0
flage = 0
thread_list=[]
def main():
    parser = optparse.OptionParser(u"usage%prog -n '<IP 数量>' [-f '<保存的文件名>'] [-t '<进程数(默认为30)>'] [-p '<端口号>(用','分割)']")
    parser.add_option('-n',dest="IPnum",type="string",help=u'要抓取的ip数量')
    parser.add_option('-f',dest="FileName",type="string",help=u'要保存的文件名')
    parser.add_option('-t',dest="threadnum",type="int",help=u"验证代理线程数量(验证专用)")
    parser.add_option('-p',dest="ports",type='string',help=u"要扫描的端口号，用','分割")
    parser.add_option('-y',dest="filen",type="string",help=u"需要验证的文件名")
    (options,args)= parser.parse_args()
    if options.filen != None and options.threadnum != None and options.IPnum == None and options.FileName == None and options.ports == None:
        filen = options.filen
        threadnum = options.threadnum
        try:
            f = open(filen,'r')
        except IOError as e:
            print u"%s不存在，请检查输入的文件名" % (filen)
        while True:
            line = f.readline()
            if line:
                line = line.strip('\n')
                iplist.append(line)
            else:
                break
        f.close()
        for ip in iplist:
            t = threading.Thread(target=validateIP,args=(filen,ip))
            thread_list.append(t)
        for t in thread_list:
            if len(threading.enumerate()) < threadnum:
                t.start()
            else:
                time.sleep(1)

"""
    #判断用户输入
    if options.IPnum == None:
        print parser.usage
        print u"请输入要提取的ip数量"
        exit()
    else:
        IPnum = options.IPnum
    if options.FileName == None:
        print u"文件名默认为ip.txt"
        FileName = "ip.txt"
    else:
        FileName = options.FileName
    if options.threadnum == None:
        print u"进程默认为30"
        threadnum = 30
    else:
        threadnum = options.threadnum
    if options.ports == None:
        print u"端口默认为['80','8080','3128','8081','9080']"
        ports = ['80','8080','3128','8081','9080']
    else:
        ports = str(options.ports).split(',')
    #判断用户的选择
"""
if __name__ == '__main__':
    main()
