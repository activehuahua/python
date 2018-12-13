#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep2.py
@Time    : 2018/12/11 10:56
@desc   :
'''

from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))