# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : string_list.py
@Time    : 2018/11/15 18:08
'''


def list_sort_by_length():
    list = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
    list.sort(key=lambda ele: len(ele))  # 按元素长度顺序升序排列
    print("升序:", list)

    list.sort(key=lambda ele: len(ele), reverse=True)  # 按降序排列
    print("降序:", list)

def two_d_list_sort():
    list=[ ["1","c++","demo"],
           ["1","c","test"],
           ["2","java",""],
           ["8","golang","google"],
           ["4","python","gil"],
           ["5","swift","apple"]
    ]
    list.sort(key=lambda ele:ele[0])# 根据第1个元素排序
    print(list)
    list.sort(key=lambda ele:ele[1]) #先根据第2个元素排序
    print(list)
    list.sort(key=lambda ele:ele[1]+ele[0]) #先根据第2个元素排序，再根据第1个元素排序
    print(list)



if __name__ == '__main__':
    two_d_list_sort()
    list_sort_by_length()
