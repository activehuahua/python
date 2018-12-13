#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-cookie.py
@Time    : 2018/12/13 17:52
@desc   :
'''

import  requests

r=requests.get("https://www.baidu.com")
print(r.cookies)
#
for key,value in r.cookies.items():
    print(key+'='+value)