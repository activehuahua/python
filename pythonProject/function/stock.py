#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"
import re
import urllib.request
from colorama import init, Fore
from time import sleep

from bs4 import BeautifulSoup


def content(url):
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    return html


def htmlData(url, pcre):
    soap = BeautifulSoup(content(url), 'html5lib', from_encoding='gbk')
    msg = re.findall(pcre, str(soap))[0]
    return msg


def main():
    stockcodes = ['s_sh000001', 's_sz399001', 's_sz399006', 's_sz399005', 's_sz159915',
                  's_sz002431', 's_sz300465', 's_sz300059', 's_sz300033', 's_sz300431', 's_sz002769', 's_sz300469',
                  's_sh600707', 's_sz300294', 's_sz002273', 's_sz002477', 's_sh600518','s_sh510500', 's_sh510300']
    print('#'*90)
    print(Fore.YELLOW + "股票名称", "\t\t", Fore.YELLOW + "最新价", "\t\t", Fore.YELLOW + "涨跌额", "\t\t", Fore.YELLOW + "涨跌幅", "\t\t",
          Fore.YELLOW + "成交量", "\t\t", Fore.YELLOW + "成交额")
    for stockcode in stockcodes:
        urlstr = "http://hq.sinajs.cn/rn=1427697590184&list=%s" % stockcode
        pcre = r'="(.*?)";'
        data = content(urlstr)
        # d = list(data)[0].decode('gbk').split("\"")[1].split(',')
        d=htmlData(url=urlstr,pcre=pcre).split(',')
        if float(d[2]) > 0:
            print('-'*90)
            print(Fore.RED + d[0].ljust(4), "\t\t", Fore.RED + d[1].ljust(8), "\t\t", Fore.RED + d[2].ljust(8), "\t\t", Fore.RED + (d[3]+'%').ljust(8), "\t\t",
                  Fore.BLUE + d[4].ljust(8), "\t\t", Fore.BLUE + d[5].ljust(8))
        elif float(d[2]) == 0:
            print('-'*90)
            print(Fore.WHITE + d[0].ljust(4), "\t\t", Fore.WHITE + d[1].ljust(8), "\t\t", Fore.WHITE + d[2].ljust(8), "\t\t", Fore.WHITE + (d[3]+'%').ljust(8), "\t\t",
                  Fore.BLUE + d[4].ljust(8), "\t\t", Fore.BLUE + d[5].ljust(8))
        else:
            print('-'*90)
            print(Fore.GREEN + d[0].ljust(4), "\t\t", Fore.GREEN + d[1].ljust(8), "\t\t", Fore.GREEN + d[2].ljust(8), "\t\t", Fore.GREEN + (d[3]+'%').ljust(8), "\t\t",
                  Fore.BLUE + d[4].ljust(8), "\t\t", Fore.BLUE + d[5].ljust(8))

main()

# if __name__ == "__main__":
#     urlstr = "http://hq.sinajs.cn/rn=1427697590184&list=s_sz300294"
#     pcre = r'="(.*?)";'
#     d=htmlData(url=urlstr,pcre=pcre).split(',')
#     print(d)