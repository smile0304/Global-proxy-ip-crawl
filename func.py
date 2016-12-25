# -*- coding: utf-8 -*-
import random
import urllib
import re
import socket
import urllib2
flage=0
"""随机生成全球任意ip"""
"""返回生成的任意ip"""
def globalip():
    ip1 = random.randint(1,223)
    ip2 = random.randint(0,255)
    ip3 = random.randint(0,255)
    ip4 = random.randint(0,255)
    ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
    return ip
"""获取当前ip"""
"""
    返回当前的ip
"""
def getip():
    URL = "http://1212.ip138.com/ic.asp"
    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    try:
        response = urllib.urlopen(URL)
    except urllib2.URLError,e:
        print u"网络异常,请检查网络连接"
    except urllib2.HTTPError,e:
        print u"网络异常,请检查网络连接"
    html = response.read()
    for ip in reip.findall(html):
        return ip

"""验证代理"""
"""
    需要参数：ip     ip
            port   端口
    返回可用的代理
        例如: 192.168.1.1:8080
"""
def ProxyVerification(ip,port):
    socket.setdefaulttimeout(10)
    URL = "http://blog.smilehacker.net"
    proxy_host = "http://"+ip+":"+port
    proxy = {"http":proxy_host}
    proxy = urllib2.ProxyHandler({"http":ip+":"+port})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    try:
        response = urllib2.urlopen('http://blog.smilehacker.net')
    except urllib2.URLError,e:
        print "[-]invalid proxy---->%s:%s" % (ip,port)
        exit()
    except urllib2.HTTPError,e:
        print u"网络异常,请检查网络连接"
        exit()
    html =response.read()
    if html:
        print "[+]find proxy------->%s:%s" % (ip,port)
        proxy = ip + ":" + port
        return proxy
    else:
        print "[-]invalid proxy---->%s:%s" % (ip,port)
"""
保存可用的代理ip
    filename    要保存的文件名
    iplist      验证成功的ip列表
"""
def writeip(filename,ipandport):
    f = open(filename,'w')
    if iplist:
        for ip in iplist:
            f.write(ip+"\n")
    f.close()
    print u"%s已写入完成!" %(filename)
"""
    主进程方法
    neednum     一共需要的ip数量
    filename    要保存的文件名
    ports       端口列表
"""
def run(filename,ports):
    ip = globalip()
    for port in ports:
        ip=ProxyVerification(ip,port)
        if ip != None:
            writeip(filename,ip)
            getnum()
"""
判断ip的总数量
    返回 ip的总数量
"""
def getnum():
    flage = flage+1
    return flage
