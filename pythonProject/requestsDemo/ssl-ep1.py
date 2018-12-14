#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : ssl-ep1.py
@Time    : 2018/12/14 13:48
@desc   :
'''
import  requests

response=requests.get('https://www.12306.cn')
print(response.status_code)