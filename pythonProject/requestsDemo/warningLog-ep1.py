#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : warningLog-ep1.py
@Time    : 2018/12/14 13:52
@desc   :
'''

import logging
import requests
import urllib3
logging.captureWarnings(True)
response=requests.get("http://www.12306.cn",verify=False)
print(response.status_code)

urllib3.disable_warnings()
response=requests.get("http://www.12306.cn",verify=False)
print(response.status_code)
