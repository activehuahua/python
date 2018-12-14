#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : auth-ep1.py
@Time    : 2018/12/14 14:36
@desc   :
'''
import requests
from requests.auth import HTTPBasicAuth

username='hudson'
password='123456'
url='http://172.28.1.236:8080/viewvc/ProductCode/'

r=requests.get(url,auth=(username,password))
print(r.status_code)