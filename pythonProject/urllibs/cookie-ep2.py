#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : cookie-ep2.py
@Time    : 2018/12/11 15:52
@desc   :
'''

import urllib.request,http.cookiejar

cookie=http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))