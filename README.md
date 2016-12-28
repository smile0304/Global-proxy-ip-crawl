# Global-proxy-ip-crawl
<h1>爬去全球代理ip</h1>


使用环境:

            python2
使用前需要安装：<br />
    	
        
			pip install beautifulsoup4
		
使用方法：

    python GpipC.py
    
      -h, --help     show this help message and exit
      -n IPNUM       要抓取的ip数量
      -f FILENAME    保存验证完成的文件名
      -j PROCESSNUM  随机抓取要启动的进程数(随机抓取专用)
      -t THREADNUM   验证代理线程数量(验证专用)
      -p PORTS       要扫描的端口号，用','分割
      -y FILEN       需要验证的文件名
    
    "验证代理ip模块"
    "
    -y "要验证的文件名"
    -t "要启动的线程"
    -f "验证通过，保存文件地址"
    "

    "爬去代理ip并验证模块"
    "
    '-n'      "要提取IP的数量"
    '-f'      "验证完成的代理IP保存地址"
    '-j'      "当网页抓取的代理不够时，自行生成代理IP的进程数"
    '-t'      "验证代理IP启动的线程数"
    '-p'      "当网页抓取的代理不够时，自行生成代理ip要扫描的端口号"
    "
		
