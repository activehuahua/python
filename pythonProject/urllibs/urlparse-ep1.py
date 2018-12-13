#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : urlparse-ep1.py
@Time    : 2018/12/11 17:04
@desc   :
'''

from urllib.parse import urlparse

result=urlparse('http://www.baidu.com/index.htm;user?id=5#comment')
print(result)
for item in range(len(result)):
    print(result[item])