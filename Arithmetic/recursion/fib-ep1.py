#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : fib-ep1.py
@Time    : 2018/12/20 10:08
@desc   :递归时候插入字典，避免重复运算
'''

dict={}

def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    if n in dict.keys():
        print(f'从字典获取数据 {n}')
        return dict[n]
    ret=fab(n - 1) + fab(n - 2)
    print(f'插入数据{n}：{ret}到字典获')
    dict[n]=ret
    return ret


if __name__=='__main__':
    n=1000
    #print(fab(n))
    for i in range(1,n+1):
        print(fab(i))