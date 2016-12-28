# -*- coding: utf-8 -*-
import random
import urllib
from bs4 import BeautifulSoup
import re
import socket
import urllib2
import multiprocessing
import threading
"""进程锁"""
lock = multiprocessing.Lock()
"""线程信号量"""
mutex = threading.Lock()
"""定义请求头"""
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
"""随机生成全球任意ip"""
"""返回生成的任意ip"""


def globalip():
    ip1 = random.randint(1, 223)
    ip2 = random.randint(0, 255)
    ip3 = random.randint(0, 255)
    ip4 = random.randint(0, 255)
    ip = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
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
    except urllib2.URLError, e:
        print u"网络异常,请检查网络连接"
    except urllib2.HTTPError, e:
        print u"网络异常,请检查网络连接"
    html = response.read()
    for ip in reip.findall(html):
        return ip
"""
验证随机生成代理
	传入参数:
                fileObject 一个文件对象
				ip	ip地址
				ports 端口号列表
"""


def ProxyVerification(fileObject, ip, ports):
    url = "http://ip.chinaz.com/getip.aspx"
    socket.setdefaulttimeout(3)
    for port in ports:
        proxy_host = "http://" + ip + ":" + port
        proxy_temp = {"http": proxy_host}
        proxy = ip + ":" + port
        try:
            res = urllib.urlopen(url, proxies=proxy_temp).read()
            mutex.acquire()
            print "[+]find proxy------->%s:%s" % (ip, port)
            writewebip(fileObject, proxy)
            mutex.release()
        except Exception, e:
            mutex.acquire()
            print "[-]Nothing proxy------->%s:%s" % (ip, port)
            mutex.release()
"""
    验证网页端抓取的代理
    fileObject 一个文件对象
    ip  一个代理ip的列表
    [192.168.0.0:8080,127.0.0.1:1111]
"""


def validateIP(fileObject, ip):
    url = "http://ip.chinaz.com/getip.aspx"
    socket.setdefaulttimeout(3)
    proxy_host = "http://" + ip
    proxy_temp = {"http": proxy_host}
    '''上锁'''
    try:
        res = urllib.urlopen(url, proxies=proxy_temp).read()
        mutex.acquire()
        print "[+]find proxy------->%s" % (ip)
        writewebip(fileObject, ip)
        '''解锁'''
        mutex.release()
    except Exception, e:
        mutex.acquire()
        print "[-]useless proxy---->%s" % (ip)
        mutex.release()
"""
保存可用的代理ip
    filename    要保存的文件名
    iplist      验证成功的ip列表
"""


def writeip(filename, iplist):
    try:
        f = open(filename, 'w')
    except Exception, e:
        print u"%s不存在，请检查输入的文件名" % (filename)
        exit(0)
    if iplist:
        for ip in iplist:
            f.write(ip + "\n")
    f.close()
    print u"%s已写入完成!" % (filename)
"""
    验证ip完成后的写入方法
    filename    要保存的文件名
    ip          要写入的ip
"""


def writewebip(fileObject, ip):
    fileObject.write(ip + "\n")
"""
    主进程方法
    neednum     一共需要的ip数量
    filename    要保存的文件名
    ports       端口列表
"""


def run(filename, ports):
    ip = globalip()
    for port in ports:
        ip = ProxyVerification(ip, port)
        if ip != None:
            writeip(filename, ip)
            getnum()
"""
    url="http://www.xicidaili.com/nn/"
	在网页中抓取代理ip
    返回
        proxy   一个ip列表
"""


def getxiciproxyip():
    proxy = []
    for i in range(1, 5):
        try:
            url = 'http://www.xicidaili.com/nn/' + str(i)
            req = urllib2.Request(url, headers=header)
            res = urllib2.urlopen(req).read()
            soup = BeautifulSoup(res)
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
                proxy.append(ip_temp)
        except:
            continue
    return proxy
"""
    获取代理666的ip
    在网页中抓取代理ip
    返回  一个ip列表
"""


def get666ip():
    proxy = []
    try:
        url = "http://ttvp.daxiangip.com/ip/?tid=xxxxxxxxx&num=5000"
        req = urllib2.Request(url, headers=header)
        html = urllib2.urlopen(req).read()
        proxy = html.split('\r\n')
    except:
        print "网络连接失败"
    return proxy
"""
    读取文件的行数
    f   一个文件对象
    返回: 文件的行数
"""


def readline(fileObject):
    num = len(fileObject.readlines())
    return num
