'''
桶排序（Bucket sort）
'''
from sort import quickSort
from typing import List

def bucket_sort(A: List[int]):
    #求A中最大数
    bucketNum=max(A)//10+1
    #T=[[],[],[],[],[]]
    #创建占位空list
    T=[[] for i in range(bucketNum)]

    #遍历数组，进行分组
    for i in range(len(A)):
        #取对应的桶的num
        j=A[i]//10
        T[j].append(A[i])

   #遍历每个桶，进行快速排序
    for i in range(len(T)):
        quickSort.quick_sort(T[i])
    print(T)

if __name__ == '__main__':
    A=[22,5,11,41,45,26,29,10,7,8,30,27,42,43,40]
    bucket_sort(A)
    A = [5, 5, 11, 11, 45, 26, 29, 10, 7, 8, 30, 30, 42, 43, 40]
    bucket_sort(A)