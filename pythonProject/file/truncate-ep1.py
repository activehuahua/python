#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : truncate-ep1.py
@Time    : 2018/12/5 14:30
'''

#!/usr/bin/python3

fo = open("runoob.txt", "r+")
print ("文件名: ", fo.name)

line = fo.readline()
print ("读取行: %s" % (line))

fo.truncate()
line = fo.readlines()
print ("读取行: %s" % (line))

# 关闭文件
fo.close()