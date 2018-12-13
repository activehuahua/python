#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : waterHeater.py
@Time    : 2018-12-13
@desc   :观察者设计模式基类
'''
class Observable:
    def __init__(self):
        self.__obervers = []

    def addObserver(self, observer):
        self.__obervers.append(observer)

    def removeObserver(self, observer):
        self.__obervers.remove(observer)

    def notifyObservers(self, object=0):
        for ob in self.__obervers:
            ob.update(self, object)


class Observer:
    def update(self, observer, object):
        pass