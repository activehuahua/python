#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : cookies-ep1.py
@Time    : 2018/12/11 15:33
@desc   :Cookie 操作
'''

import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name +"="+item.value)

filename = 'cookie.txt'
#cookie=http.cookiejar.MozillaCookieJar()
cookie=http.cookiejar.LWPCookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(filename)