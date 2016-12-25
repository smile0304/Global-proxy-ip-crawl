# -*- coding: utf-8 -*-
import optparse
from func import globalip,getip,ProxyVerification,writeip,run,getnum
from multiprocessing import Pool
iplist = []
num = 0
flage = 0
def main():
    parser = optparse.OptionParser(u"usage%prog -n '<IP 数量>' [-f '<保存的文件名>'] [-t '<进程数(默认为30)>'] [-p '<端口号>(用','分割)']")
    parser.add_option('-n',dest="IPnum",type="string",help=u'要抓取的ip数量')
    parser.add_option('-f',dest="FileName",type="string",help=u'要保存的文件名')
    parser.add_option('-t',dest="threadnum",type="int",help=u"要启动的进程数量")
    parser.add_option('-p',dest="ports",type='string',help=u"要扫描的端口号，用','分割")
    (options,args)= parser.parse_args()
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
    pool = Pool(threadnum)
    if IPnum > getnum():
        pool.apple_async(func=run,args=(FileName,ports))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
