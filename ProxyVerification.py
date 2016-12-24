# -*- coding: utf-8 -*-
import urllib
import re
import socket
import urllib2
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
        print "网络异常,请检查网络连接"
    except urllib2.HTTPError,e:
        print "网络异常,请检查网络连接"
    html = response.read()
    for ip in reip.findall(html):
        return ip

"""验证代理"""
"""
    需要参数：ip，端口
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
        print "网络异常,请检查网络连接"
        exit()
    html =response.read()
    if html:
        print "[+]find proxy------->%s:%s" % (ip,port)
        proxy = ip + ":" + port
        return proxy
    else:
        print "[-]invalid proxy---->%s:%s" % (ip,port)
