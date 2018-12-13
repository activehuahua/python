#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : urlencode-ep1.py
@Time    : 2018/12/11 18:01
@desc   : 序列化和反序列化参数
'''

from urllib.parse import urlencode, parse_qs,parse_qsl
import re

param = {'name': 'germey', 'age': '22'}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(param)
print(url)

query = 'name=germey&age=22'
print(parse_qs(query))
print(parse_qsl(query))
query = r'http://www.baidu.com?name=germey&age=22'
queryObj = re.match(r'([0-9a-zA-Z./:]+[\?])(.*)', query)
query = queryObj.group(2)
#query = query[1:]
print(parse_qs(query))
