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
"""
验证随机生成代理
	传入参数:
				ip	ip地址
				port 端口号
	返回参数：
			返回可用的代理地址
			127.0.0.1:8080
"""
def ProxyVerification(ip,port):
	url = "http://ip.chinaz.com/getip.aspx"
	socket.setdefaulttimeout(3)
	proxy_host= "http://"+ip+":"+port
	proxy_temp = {"http":proxy_host}
	proxy = ip+":"+port
	print "[*] test proxy------->%s:%s" % (ip,port)
	try:
		res = urllib.urlopen(url,proxies=proxy_temp).read()
		print "[+]find proxy------->%s:%s" % (ip,port)
		return proxy
	except Exception,e:
		print "[-]Nothing proxy------->%s" %(ip)
"""
    验证网页端抓取的代理
    传入 一个代理ip的列表
    [192.168.0.0:8080,127.0.0.1:1111]
"""
def validateIP(filename,ip):
    url = "http://ip.chinaz.com/getip.aspx"
    socket.setdefaulttimeout(3)
    proxy_host = "http://"+ip
    proxy_temp= {"http":proxy_host}
    '''上锁'''
    mutex.acquire()
    print "[*] test proxy--------->%s" % (ip)
    try:
        res = urllib.urlopen(url,proxies=proxy_temp).read()
        print "[+]find proxy------->%s" % (ip)
        writewebip(filename,ip)
        '''解锁'''
        mutex.release()
    except Exception,e:
        print "[-]Nothing proxy------->%s" %(ip)
        '''解锁'''
        mutex.release()

"""
保存可用的代理ip
    filename    要保存的文件名
    iplist      验证成功的ip列表
"""
def writeip(filename,iplist):
    f = open(filename,'w')
    if iplist:
        for ip in iplist:
            f.write(ip+"\n")
    f.close()
    print u"%s已写入完成!" %(filename)
"""
    验证ip完成后的写入方法
    filename    要保存的文件名
    ip          要写入的ip
"""
def writewebip(filename,ip):
    f = open(filename,'w')
    f.write(ip+"\n")
    f.close
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
"""
    url="http://www.xicidaili.com/nn/"
	在网页中抓取代理ip
    返回
        proxy   一个ip列表
"""
"""
def getxiciip():
	proxy = []
	for i in range(1,10):
        try:
            url = 'http://www.xicidaili.com/nn/'+str(i)
			req = urllib2.Request(url,headers=header)
			res = urllib2.urlopen(req).read()
			soup = BeautifulSoup(res)
			ips = soup.findAll('tr')
            for x in range(1,len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = tds[1].contents[0]+":"+tds[2].contents[0]
                proxy.append(ip_temp)
		except:
			continue
		return proxy
        """
"""
    获取代理666的ip
    在网页中抓取代理ip
    返回  一个ip列表
"""
def get666ip():
    proxy = []
    try:
        url = "http://ttvp.daxiangip.com/ip/?tid=557671197349291&num=5000"
        req = urllib2.Request(url,headers=header)
        html = urllib2.urlopen(req).read()
        proxy = html.split('\r\n')
    except:
        print "网络连接失败"
    return proxy
