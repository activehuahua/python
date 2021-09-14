# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : using_sys.py
@Time    : 2018/12/5 9:54
'''

import sys,os

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

print(sys.path[0])
print(os.getcwd())
