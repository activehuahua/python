#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : quickSort.py
@Time    : 2018/12/26 10:15
@desc   :
'''

from typing import List
import  random,time
from datetime import datetime

def quick_sort(A: List[int]):
    quick_sort_c(A, 0, len(A) - 1)


def quick_sort_c(A: List[int], low: int, high: int):
    if low >= high:
        return
    #print(A)
    mid = partition(A, low, high)
    quick_sort_c(A, low, mid - 1)
    quick_sort_c(A, mid + 1, high)


def partition(A: List[int], low: int, high: int):
    pivot = A[high]
    i ,j= low,low
   # j = i
    for j in range(low,high) :
        if A[j] < pivot:
            A[i],A[j] = A[j],A[i]
            i += 1
            #print(A)
    A[i],A[high]=A[high],A[i]
    #print(A)
    return i

def get_random_list(count):

    for i in range(count):
        number=random.randint(1,10000)
        dataList.append(number)
    #print(dataList)
    return dataList

if __name__=='__main__':
    a=[6,11,3,9,8]
    quick_sort(a)
    print(a)
    a=[11,8,3,9,7,1,2,5]
    quick_sort(a)
    print(a)
    a=[6,8,7,6,3,5,9,4]
    quick_sort(a)
    print(a)


    # dataList=[]
    # dataList=get_random_list(10000)
    #
    # begin_time = datetime.now()
    # quick_sort(dataList)
    # end_time=datetime.now()
    #
    # print('耗时：',end_time-begin_time)
    # print(dataList)