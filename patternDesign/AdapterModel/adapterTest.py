#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : adapterTest.py
@Time    : 2018/12/14 10:04
@desc   :
'''
from AdapterModel.HighPerson import HighPerson
from AdapterModel.DecoratePerson import DecoratePerson

def canPlayReceptionist(person):
    return person.getHeight() >= 165



lira =HighPerson("Lisa",172)

print(lira.getName() + "身高" + str(lira.getHeight()) + "，完美如你，天生的美女！")
print("是否适合做接待员：", "符合" if canPlayReceptionist(lira) else "不符合")
print()

demi = DecoratePerson("Demi",159)
print(demi.getName() + "身高" + str(demi.getHeight()) + "在高跟鞋的适配下，你身高不输高圆圆，气质不输范冰冰！")
print("是否适合做接待员：", "符合" if canPlayReceptionist(demi) else "不符合")

