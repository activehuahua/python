# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:34
# @Author  : zhaojianghua
# @File    : bSearch4.py
# @Software: PyCharm
# @Desc    : 查找第一个大于等于给定值的元素
#

from typing import List

def binary_search_normal_4(A:List[int],goal_num):
    if goal_num>A[len(A)-1]:
        print(f'第一个目标数字大于{goal_num}未找到！')
        return None,0
    search_count=1
    low=0
    high=len(A)

    while low<=high:
        mid=low+(high-low)//2
        if A[mid]>=goal_num:
            if (mid==0 or A[mid-1]<goal_num):
                print(f'第一个目标数字大于{goal_num}找到, 在{mid+1}位置上！执行搜索{search_count}次')
                return mid, search_count
            else :
                high=mid-1
        else:
            low=mid+1
        search_count+=1

    print(f'第一个目标数字大于{goal_num}未找到！')
    return None,0


if __name__ == '__main__':
    A=[1,2,4,5,6,8,8,8,11,18]
    # for i in range(len(A)):
    #     goal_num=A[i]
    #     binary_search_normal_1(A,goal_num)

    goal_num =12
    binary_search_normal_4(A, goal_num)
