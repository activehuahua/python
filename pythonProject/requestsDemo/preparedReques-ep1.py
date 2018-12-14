#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : preparedReques-ep1.py
@Time    : 2018/12/14 14:45
@desc   :
'''
import requests
from requests import Request,Session

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}

s=Session()
req=Request('POST',url,data=dict,headers=headers)
pre=s.prepare_request(req)
r=s.send(pre)

print(r.text)