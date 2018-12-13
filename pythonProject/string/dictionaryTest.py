# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : dictionaryTest.py
@Time    : 2018/11/14 17:25
'''
# !/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(list(tinydict.keys()))  # 输出所有键
print(list(tinydict.values()))  # 输出所有值