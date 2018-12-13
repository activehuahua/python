#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : opener-ep1.py
@Time    : 2018/12/11 15:01
@desc   :自动填充用户名及密码
'''

from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
from urllib.error import URLError

username='hudson'
password='123456'
url='http://172.28.1.236:8080/viewvc/ProductCode/'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler= HTTPBasicAuthHandler(p)
opener=build_opener(auth_handler)

try:
    result=opener.open(url)
    html=result.read().decode('UTF-8')
    print(html)
except URLError as e:
    print(e.reason)