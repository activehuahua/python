# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 17:34
# @Author  : zhaojianghua
# @File    : bSearch3.py
# @Software: PyCharm
# @Desc    : 查找最后等于给定值的元素

from typing import List

def binary_search_normal_3(A:List[int],goal_num):
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
            if (mid==high or A[mid+1]!=goal_num):
                print(f'目标数字{goal_num}找到, 在{mid+1}位置上！执行搜索{search_count}次')
                return mid,search_count
            else:
                low=mid+1
        search_count+=1

    print(f'目标数字{goal_num}未找到！')
    return None,0


if __name__ == '__main__':
    A=[1,2,4,5,6,8,8,8,11,18]
    # for i in range(len(A)):
    #     goal_num=A[i]
    #     binary_search_normal_1(A,goal_num)

    goal_num =8
    binary_search_normal_3(A, goal_num)
