#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : session-ep1.py
@Time    : 2018/12/14 13:38
@desc   :
'''

import requests

s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)
