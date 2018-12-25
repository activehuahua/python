#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : json-ep2.py
@Time    : 2018/12/25 19:15
@desc   :
'''

import  json

str='''
[{
    "name":"zhaojianghua",
    "gender":"male"
},{
    "name":"alex",
    "gender":"female"
}]
'''

data=json.loads(str)
print(data)
print(type(data))

with open('json.txt','w') as f:
    f.write(json.dumps(data,indent=2))