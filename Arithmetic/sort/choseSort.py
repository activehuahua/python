#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     choseSort
   Description :
   Author :       zhaojianghua
   date：          2018/12/23
'''

import  random,time
from datetime import datetime
dataList=[]

def get_random_list(count):

    for i in range(count):
        number=random.randint(1,10000)
        dataList.append(number)
    #print(dataList)
    return dataList

def choseSort(list):
    n = len(dataList)

    for i in range(n):
        min = list[i]
        min_pos = i
        for j in range(i + 1, n):

            if list[j] < min:
                min = list[j]
                min_pos = j
                continue
        list[min_pos] = list[i]
        list[i] = min

        #print(list)


if __name__ == '__main__':

    dataList=get_random_list(10000)
    begin_time=datetime.now()
    choseSort(dataList)
    end_time=datetime.now()

    print('耗时：',end_time-begin_time)
    print(dataList)