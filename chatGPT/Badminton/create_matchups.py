#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : create_matchups.py
@Time    : 2023/3/27
@desc   : 羽毛球对阵秩序表
'''
import math

import pandas as pd


class createMatchups:
    def __init__(self,field_num,team_num):
        self.__field_num=field_num
        self.__team_num=team_num
        self.__group_A=[]
        self.__group_B=[]
        self.__totalCount=0
        self.__roundCount=0
        self.__roundNames=[]
        self.__field_name=[]
        self.__matchups=[]

    '''初始化两个俱乐部的队伍编号'''
    def initInfo(self):
        for index in range(self.__field_num):
            self.__field_name.append('场地'+str(index))

        for index in range(self.__team_num):
            self.__group_A.append('A'+str(index))
            self.__group_B.append('B' + str(index))

        '''获取轮次数'''
        count_group = self.__team_num
        self.__totalCount= count_group * count_group
        self.__roundCount = math.ceil(self.__totalCount /self.__field_num)

        '''获取轮数名称'''
        for index in range(self.__roundCount ):
            self.__roundNames.append('第' + str(index + 1) + '轮')



    '''获取所有对局数'''

    def getAllMatchups(self):
        matchups = []
        for index_a in range(len(self.__group_A)):
            result = self.__group_A[index_a:] + self.__group_A[0:index_a]
            for index_b in range(len(self.__group_B)):
                matchups.append(result[index_b] + ":" +self.__group_B[index_b])

    '''输出到excel中'''

    def export2Excel(self):
        df = pd.DataFrame(columns=self.__field_name, index=self.__roundNames)
        index = 0
        for round_index, round_name in enumerate(self.__roundNames):
            for field_index, field_name in enumerate(self.__field_name):
                df.at[round_name, field_name] = self.__matchups[index]
                print("[index=%d],%s" % (index, self.__matchups[index]))
                index = index + 1
                if index >= self.__totalCount:
                    self.__matchups.append('')

        df.to_excel('matchups.xlsx')

if __name__ == '__main__':
    newMatchups=createMatchups(4,7)
    newMatchups.initInfo()
    newMatchups.getAllMatchups()
    newMatchups.export2Excel()