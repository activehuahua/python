#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : fib.py
@Time    : 2018/12/20 9:34
@desc   :
'''


def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    ret=fab(n - 1) + fab(n - 2)
    return ret


if __name__=='__main__':
    n=8
    print(fab(n))
    for i in range(1,n+1):
        print(fab(i),end=' ')
