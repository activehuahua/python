#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : quickSort_K.py
@Time    : 2018/12/26 14:19
@desc   : 找到排列中第K大数字
'''

from typing import List
import  random,time
from datetime import datetime

def quick_sort(A: List[int],K):
    quick_sort_c(A, 0, len(A) - 1,K)


def quick_sort_c(A: List[int], low: int, high: int,K:int):
    if low > high:
        return
    #print(A)
    mid = partition(A, low, high)



    if K-1>mid:
            quick_sort_c(A, mid + 1, high, K)
    else:
            quick_sort_c(A, low, mid - 1, K)

    if K-1==mid or mid==0:
            print(A[K-1])



def partition(A: List[int], low: int, high: int):
    pivot = A[high]
    i ,j= low,low
    for j in range(low,high) :
        if A[j] >= pivot :
            A[i],A[j] = A[j],A[i]
            i += 1
            #print(A)
    A[i],A[high]=A[high],A[i]
    #print(A)
    return i


if __name__=='__main__':
    # a=[6,11,3,9,8]
    # quick_sort(a,3)
    # print(a)
    # a=[11,8,3,9,7,1,2,5]
    # quick_sort(a,1)
    # print(a)
    # a=[6,8,7,6,3,5,9,4]
    # quick_sort(a,6)
    # print(a)
    a=[6,1,3,5,7,2,4,9,11,8]
    quick_sort(a,1)
    print(a)

