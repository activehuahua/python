#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     insertionSort
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

def insertionSort(list):
    n=len(dataList)

    for i in range(1,n):
        value=list[i]
        j=i-1
        while j>=0:
            if list[j]>value:
                list[j+1]=list[j]
                j-=1
            else:
                break
        list[j+1]=value
        #print(list)


if __name__=='__main__':
    list=get_random_list(10000)
    begin_time=datetime.now()
    insertionSort(list)

    end_time=datetime.now()

    print('耗时：',end_time-begin_time)
    print(dataList)

