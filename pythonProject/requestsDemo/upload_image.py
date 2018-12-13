#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : upload_image.py
@Time    : 2018/12/13 17:37
@desc   :
'''
import  requests

files={'file':open('favicon.ico','rb')}
r= requests.post("http://httpbin.org/post",files=files)

print(r.text)