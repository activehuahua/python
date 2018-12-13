#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : proxy-ep1.py
@Time    : 2018/12/11 15:23
@desc   :
'''

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_handler=ProxyHandler({
    'http':'https://125.70.11110.191:123456'
})

opener =build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com',timeout=0.01)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(type(e.reason))
    print(e.reason)