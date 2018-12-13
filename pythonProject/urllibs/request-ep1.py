#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep1.py
@Time    : 2018/12/11 10:17
@desc   :
'''

import urllib.request

request= urllib.request.Request('http://www.ip168.com/')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')
response = urllib.request.urlopen(request)
print(response.read().decode('UTF8'))

#print(request.get_header('User-Agent'))