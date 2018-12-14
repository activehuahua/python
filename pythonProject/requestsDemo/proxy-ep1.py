#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : proxy-ep1.py
@Time    : 2018/12/14 14:09
@desc   :
'''

import requests

proxies = {
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080"
}

requests.get("http://www.baidu.com",proxies=proxies)
