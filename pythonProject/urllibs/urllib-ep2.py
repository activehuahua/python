#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : urllib-ep2.py
@Time    : 2018/12/10 17:48
@desc   :
'''

from urllib import  request,parse,error
from bs4 import BeautifulSoup
import socket



data =  bytes(parse.urlencode({'word':'hello'}),encoding='utf-8')
response = request.urlopen('http://httpbin.org/post',data=data,timeout=1)
s= response.read()
soup= BeautifulSoup(s,'lxml')

print(soup.p.string)

try:
    response = request.urlopen('http://httpbin.org/post',  timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')