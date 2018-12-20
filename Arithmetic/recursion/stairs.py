#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : stairs.py
@Time    : 2018/12/20 10:26
@desc   :
'''
dict = {}


def stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    if n in dict.keys():
        # print(f'从字典获取数据 {n}')
        return dict[n]

    ret = stairs(n - 1) + stairs(n - 2)
    # print(f'插入数据{n}：{ret}到字典获')
    dict[n] = ret
    return ret


if __name__ == '__main__':
    n = 8
    # print(fab(n))
    for i in range(1, n + 1):
        print(stairs(i))
