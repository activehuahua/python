#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep3.py
@Time    : 2018/12/12 18:03
@desc   :
'''

import requests

r=requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)

with open('favincon.ico','wb') as f:
    f.write(r.content)