# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 9:33
# @Author  : zhaojianghua
# @File    : countSort.py
# @Software: PyCharm
# @Desc    : 计数排序

from typing import List

def counting_sort(A:List[int]):
    n=len(A)
    max_num=max(A)+1
    c=[0 for i in range(max_num)]

    #数组C 先初始化成对应数字的集合
    for i in range(n):
        c[A[i]]+=1

    for i in range(1,max_num):
        c[i]=c[i-1]+c[i]     # 从第2项开始后面一项是前面所有项累计

    i=n-1
    r=[0 for i in range(n)]
    while i>=0:    #从源list最后一位进行处理
        index=c[A[i]]-1  #从C列表中找到对应元素应插入的位置
        r[index]=A[i]    #插入值到对应的目标list中
        c[A[i]]-=1       #C列表对应位置-1，表示已经处理好一位
        i-=1             #处理源list中下一位数字
    print(r)



if __name__ == '__main__':
    A=[2,5,3,0,2,3,0,3]
    counting_sort(A)