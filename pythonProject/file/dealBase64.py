#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : dealBase64.py
@Time    : 2019/5/28 16:36
@desc   :
'''

import base64


file_path = "F:\\SilkSoftware\\testingFiles\\company.json"
data=base64.b64encode(open(file_path, "rb").read())

print (data)