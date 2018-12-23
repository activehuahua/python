#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     bubleSort
   Description :
   Author :       zhaojianghua
   date：          2018/12/23
'''

dataList=[3,5,4,1,2,6]

def bubleSort(list):
    n=len(dataList)

    for i in range(n):
        flag=False

        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=True
        print(list)
        if flag == False:
            break

if __name__=='__main__':
    print(dataList)
    bubleSort(dataList)