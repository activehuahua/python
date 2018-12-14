#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : ShortPersion.py
@Time    : 2018/12/14 9:57
@desc   :
'''

class ShortPerson:
    def __init__(self,name,height):
        self.__name=name
        self.__height=height

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return self.__height

    def getShoeHeight(self):
        return 6