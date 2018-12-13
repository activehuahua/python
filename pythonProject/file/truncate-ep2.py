#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : truncate-ep2.py
@Time    : 2018/12/5 14:33
'''

#!/usr/bin/python3

# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)

# 截取10个字节
fo.truncate(10)

str = fo.read()
print ("读取数据: %s" % (str))

# 关闭文件
fo.close()