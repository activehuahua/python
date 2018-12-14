#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : HightPerson.py
@Time    : 2018/12/14 9:51
@desc   :
'''

from AdapterModel.IHightPerson import  IHightPerson

class HighPerson(IHightPerson):
    def __init__(self,name,height):
        self.__name=name
        self.__height=height


    def getName(self):
        return self.__name

    def getHeight(self):
        return self.__height