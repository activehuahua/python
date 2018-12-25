#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : randomTeam.py
@Time    : 2018/12/21 9:00
@desc   :
'''
import random
from typing import Optional, List
girls = ['美羊羊', '晨晨', '空姐', '雾女', '晴', '青鸢']
captains = ['波哥', '途哥', '白哥', '奇哥', '张哥', '风哥']
boys1 = ['火锅', '三牛淼', '快羽', '皮皮', '林立', '黑夜']
boys2 = ['懒得', '刘豪杰', '于智远', '汉上风云', '跑车', '华哥']
boys3 = ['钟哥', '箭竹', '小刚', '蜗牛', '雾男', '笑看']
capacity = 5
group_num = 6
target_groups = []
boys = []
mans=[]


# 随机从某源列表中获取一个人
def get_one_person_from_list(list) -> str:
    length = len(list)
    if length != 0:
        position = random.randint(0, length - 1)
        person = list[position]
        list.pop(position)
        # print(list)
        return person
    return None
    numList = [x for i in range(group_num)]


def get_one_person_from_list_pos(list, pos) -> str:
    length = len(list)
    if length >= pos:
        person = list[pos - 1]
        list.pop(pos - 1)
        # print(list)
        return person
    return None
    numList = [x for i in range(group_num)]


# 随机取一个源列表
def get_random_source_group() -> List[str]:
    length = len(boys)
    position = random.randint(0, length - 1)
    return boys[position]


# 初始化目标group
def initial_groups():
    boys = [boys1, boys2, boys3]
    mans=[captains,boys1, boys2, boys3]
    for i in range(group_num):
        temp = 'group' + str(i)
        temp = []
        target_groups.append(temp)


# 获取随机group
def get_random_target_group() -> List[str]:
    position = random.randint(0, group_num)
    return target_groups[position]


# 分配一组成员到目标组中，不重复
def assign_oneGroupPeople_to_target_group(list):
    numList = [i for i in range(group_num)]
    # print(numList)
    for num in range(len(list)):
        person = get_one_person_from_list(list)
        if len(numList) != 0:
            pos = random.randint(0, len(numList) - 1)
            goup_num = numList[pos]
            numList.pop(pos)
            target_groups[goup_num].append(person)


def assign_GroupPeople_to_target_group(list):
    numList = [i for i in range(group_num)]
    while len(numList) >= 1:
        while len(list) != 0:
            person = get_one_person_from_list(list)

            ranGroupNum = random.randint(0, len(numList) - 1)
            # length=random.randint(0,len(list)-1)
            targetList = target_groups[numList[ranGroupNum]]
            if len(targetList) < capacity:
                targetList.append(person)
            if len(targetList) == capacity:
                numList.pop(ranGroupNum)


def print_all_group():
    for item in target_groups:
        print(item)


def print_all_random_group():
    print('\n')
    for item in target_groups:
        print(item[0], end=' ')
        print(item[1], end=' ')
        list = item[2:]
        for num in range(2, 5):
            person = get_one_person_from_list(list)
            print(person, end=' ')
        print('\n')


def get_oneGroup_member(str):
    length = len(captains)
    result = []
    for i in str:
        if int(i) > length:
            print('输入有误，请重新输入')
            return -1
    if length>=1:
        result.append(get_one_person_from_list_pos(captains, int(str[0])))
        result.append(get_one_person_from_list_pos(boys1, int(str[1])))
        result.append(get_one_person_from_list_pos(boys2, int(str[2])))
        result.append(get_one_person_from_list_pos(boys3, int(str[3])))
        print(result)
        print_remain()
       # print('\n')
        length = len(captains)
        # print('length=',length)
        # if length==1:
        #     result = []
        #     result.append(captains[0])
        #     result.append(boys1[0])
        #     result.append(boys2[0])
        #     result.append(boys3[0])
        #     print(result)
def print_remain():

    print('*****选手池中还剩以下这些人*****')
    # print(captains)
    # print(boys1)
    # print(boys2)
    # print(boys3)

    re_random_list(captains)
    re_random_list(boys1)
    re_random_list(boys2)
    re_random_list(boys3)

    print(captains)
    print(boys1)
    print(boys2)
    print(boys3)

def re_random_list(list):
    length=len(list)
    numList = [i for i in range(length)]
    newlist=[]
    while len(numList)>0:
        pos=random.randint(0,len(numList)-1)
        newlist.append(list[numList[pos]])
        numList.pop(pos)

    for i in range(0,len(list)):
        list[i]=newlist[i]
    #print(list)

if __name__ == '__main__':
    # 定义
    initial_groups()
    # assign_oneGroupPeople_to_target_group(captains)
    # assign_oneGroupPeople_to_target_group(girls)
    # assign_oneGroupPeople_to_target_group(boys1)
    # assign_oneGroupPeople_to_target_group(boys2)
    # assign_oneGroupPeople_to_target_group(boys3)
    # list = []
    # list.extend(boys1)
    # list.extend(boys2)
    # list.extend(boys3)
    # # print(list)
    # assign_GroupPeople_to_target_group(list)
    # print_all_group()
    # print_all_random_group()

    str=input('请输入四位抽签数字：')
    while str!="-1" :
        get_oneGroup_member(str)
        if len(captains)==0 or captains is None :
            break
        str = input('请输入四位抽签数字：')

