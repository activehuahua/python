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

captains = ['波哥', '途哥', '白哥', '奇哥', '张哥', '风哥']
girls = ['美羊羊', '晨晨', '空姐', '雾女', '晴', '青鸢']
boys1 = ['火锅', '三牛淼', '快羽', '皮皮', '林立', '黑夜']
boys2 = ['懒得', '刘豪杰', '于智远', '汉上风云', '跑车', '华哥']
boys3 = ['LZ', '箭竹', '小刚', '蜗牛', '雾男', '笑看']
capacity = 5
group_num = 6
target_groups = []
boys = []


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


# 随机取一个源列表
def get_random_source_group() -> List[str]:
    length = len(boys)
    position = random.randint(0, length - 1)
    return boys[position]


# 初始化目标group
def initial_groups():
    boys = [boys1, boys2, boys3]
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
    while len(numList)>=1:
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


if __name__ == '__main__':
    # 定义
    initial_groups()
    assign_oneGroupPeople_to_target_group(captains)
    assign_oneGroupPeople_to_target_group(girls)
    # assign_oneGroupPeople_to_target_group(boys1)
    # assign_oneGroupPeople_to_target_group(boys2)
    # assign_oneGroupPeople_to_target_group(boys3)
    list = []
    list.extend(boys1)
    list.extend(boys2)
    list.extend(boys3)
    # print(list)
    assign_GroupPeople_to_target_group(list)
    print_all_group()
