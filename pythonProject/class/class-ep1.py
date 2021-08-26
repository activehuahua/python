#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : class-ep1.py
@Time    : 2018/12/5 16:20
'''


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。 我体重%d " % (self.name, self.age, self.__weight))


# 单继承示例
class student(people):
    grade = ''
    __weight = 0

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
        self.__weight = w

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级,我体重%d " % (self.name, self.age, self.grade, self.__weight))


s = student('ken', 10, 60, 3)

s.speak()
