#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : DecoratePerson.py
@Time    : 2018/12/14 9:58
@desc   :
'''

from AdapterModel.IHightPerson import IHightPerson
from AdapterModel.ShortPersion import ShortPerson

class DecoratePerson(ShortPerson,IHightPerson):

    def getHeight(self):
        return super().getRealHeight()+super().getShoeHeight()

