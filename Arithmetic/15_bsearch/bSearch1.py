# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:34
# @Author  : zhaojianghua
# @File    : bSearch1.py
# @Software: PyCharm
# @Desc    : 常规，无重复数据的二分法
from typing import List

def binary_search_normal_1(A:List[int],goal_num):
    if goal_num>A[len(A)-1]:
        print(f'目标数字{goal_num}未找到！')
        return None,0
    search_count=1
    low=0
    high=len(A)

    while low<=high:
        mid=low+(high-low)//2
        if A[mid]>goal_num:
            high=mid-1
        elif A[mid]<goal_num:
            low=mid+1
        else:
            print(f'目标数字{goal_num}找到, 在{mid+1}位置上！执行搜索{search_count}次')
            return mid,search_count
        search_count+=1

    if search_count==len(A) and A[len(A)]!=goal_num:
        print(f'目标数字{goal_num}未找到！')
        return None,0


if __name__ == '__main__':
    A=[8,11,19,23,27,33,45,55,67,98]
    # for i in range(len(A)):
    #     goal_num=A[i]
    #     binary_search_normal_1(A,goal_num)

    goal_num =8111
    binary_search_normal_1(A, goal_num)
