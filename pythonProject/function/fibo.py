#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : fibo.py
@Time    : 2018/12/5 10:04
'''


# 斐波那契(fibonacci)数列模块
class Fib:
    def fib(n):  # 定义到 n 的斐波那契数列
        a, b = 0, 1
        while b < n:
            print(b, end=' ')
            a, b = b, a + b
        print()


    def fib2(n):  # 返回到 n 的斐波那契数列
        result = []
        a, b = 0, 1
        while b < n:
            result.append(b)
            a, b = b, a + b
        return result

    def fibTotalNum(n):
        result = []
        a, b = 0, 1
        i=1
        while(i<=n):
            result.append(b)
            a, b = b, a + b
            i+=1
        return  result