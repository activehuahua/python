#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : url-ep1.py
@Time    : 2018/12/10 16:28
@desc   :
'''

from urllib import request, response

response = request.urlopen('https://www.python.org')

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))