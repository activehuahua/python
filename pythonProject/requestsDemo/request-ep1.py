#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep1.py
@Time    : 2018/12/12 15:49
@desc   :
'''

import requests
from bs4 import BeautifulSoup

r= requests.get("http://httpbin.org/get")
# print(type(r))
# print(r.status_code)
# print(type(r.text))
print(r.text)
# print(r.cookies)

# r=requests.post("http://httpbin.org/post")
# r=requests.head("http://httpbin.org/get")
#print(r.headers)

soup=BeautifulSoup(r.text,'lxml')
#print(r.content)
print(soup.p.string)
