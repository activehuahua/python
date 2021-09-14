#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : test.py
@Time    : 2018/12/5 9:59
'''

from pythonProject.imports import support
from function.fibo import Fib

support.print_func("Runoob")
Fib.fib(10)
print(Fib.fib2(50))
print(Fib.fibTotalNum(20))
print(dir())