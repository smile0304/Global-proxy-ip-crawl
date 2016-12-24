# -*- coding:utf-8 -*-
import optparse
def main():
    parser = optparse.OptionParser("usage%prog -n <IP 数量> -f <保存的文件名>")
    parser.add_option('-n',dest="IPnum",type="string",help='要抓取的ip数量')
    parser.add_option('-f',dest="FileName",type="string",help='要保存的文件名')
    (options,args)= parser.parse_args()
    if(options.IPnum == None):
        print parser.usage
        print "请输入要提取的ip数量"
    else:
        IPnum = options.IPnum
    if(options.FileName == None):
        print "没有设置文件名，默认为ip.txt"
        FileName = "ip.txt"
    else:
        FileName = options.FileName
