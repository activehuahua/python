#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : re-ep1.py
@Time    : 2018/12/12 16:51
@desc   :
'''
import requests,re

headers ={
    'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
}

r=requests.get('http://cc.huimaifang.com/',headers=headers)
print(r.status_code)
#pattern=re.compile('<a[a-z\s"/=:._]+[\d]*.htm">([^动态].*?)</a>')
pattern=re.compile('/news/[\d]+.htm">([^动态].*)?</a>')
titles =re.findall(pattern,r.text)
print(titles )
for item in titles:
    print(item)
