#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : mergeSort.py
@Time    : 2018/12/25 10:50
@desc   :归并排序
'''


def merge_sort(A):
    merge_sort_c(A, 0, len(A) - 1)


def merge_sort_c(A, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort_c(A, low, mid)
    merge_sort_c(A, mid + 1, high)
    merge(A, low, mid, high)


def merge(A, low, mid, high):
    temp = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    start = i
    end = mid
    if (i > mid):
        start = j
        end = high
    while start <= end:
        temp.append(A[start])
        start += 1
    # k=0
    # for k in range (high-low+1):
    #      A[low+k]=temp[k]
    #
    # A[p + k] = temp[k]

    A[low:high + 1] = temp


if __name__ == '__main__':
    A = [1, 5, 6, 2, 3, 4]
    merge_sort(A)
    print(A)
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)
