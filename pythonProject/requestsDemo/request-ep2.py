#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep2.py
@Time    : 2018/12/12 16:39
@desc   :
'''

import requests,json

param ={
    "name":"geoemy",
    "age":"22"
}

r= requests.get("http://httpbin.org/get",params=param)
#print(r.text)

print(r.json())

Json=json.loads(r.text)
print(Json["headers"]["User-Agent"])