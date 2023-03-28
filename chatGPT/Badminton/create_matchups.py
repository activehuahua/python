#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : create_matchups.py
@Time    : 2023/3/27
@desc   : 羽毛球对阵秩序表
'''
import math
import os

import pandas as pd


class createMatchups:
    def __init__(self,field_num,team_num):
        '''场地数'''
        self.__field_num=field_num
        '''每个俱乐部的队伍数'''
        self.__team_num=team_num
        self.__group_A=[]
        self.__group_B=[]
        '''比赛总局数'''
        self.__totalCount=0
        '''比赛轮数'''
        self.__roundCount=0
        '''轮数名称'''
        self.__roundNames=[]
        '''场地名称'''
        self.__field_name=[]
        '''对阵表'''
        self.__matchups=[]
        '''存放的文件名'''
        self.__fileName=''

    '''初始化两个俱乐部的基础信息'''
    def initInfo(self):
        for index in range(self.__field_num):
            self.__field_name.append('场地'+str(index+1))

        for index in range(self.__team_num):
            self.__group_A.append('A'+str(index+1))
            self.__group_B.append('B' + str(index+1))

        '''获取轮次数'''
        count_group = self.__team_num
        self.__totalCount= count_group * count_group
        self.__roundCount = math.ceil(self.__totalCount /self.__field_num)

        '''获取轮数名称'''
        for index in range(self.__roundCount ):
            self.__roundNames.append('第' + str(index + 1) + '轮')
        resultPath=os.getcwd()+os.path.sep+'result'
        if os.path.exists(resultPath):
            print('已存在该文件夹')
        else:
            os.mkdir(resultPath)

        self.__fileName=resultPath+os.path.sep+'matchups_场地数'+str(self.__field_num)+'_队伍数'+str(self.__team_num)+'.xlsx'




    '''获取所有对局数'''
    def getAllMatchups(self):
        matchups = []
        for index_a in range(len(self.__group_A)):
            result = self.__group_A[index_a:] + self.__group_A[0:index_a]
            for index_b in range(len(self.__group_B)):
                self.__matchups.append(result[index_b] + ":" +self.__group_B[index_b])

    '''输出到excel中'''
    def export2Excel(self):
        df = pd.DataFrame(columns=self.__field_name, index=self.__roundNames)
        index = 0
        for round_index, round_name in enumerate(self.__roundNames):
            for field_index, field_name in enumerate(self.__field_name):
                df.at[round_name, field_name] = self.__matchups[index]
                # print("[index=%d],%s" % (index, self.__matchups[index]))
                index = index + 1
                if index >= self.__totalCount:
                    self.__matchups.append('')
        # filename='matchups_场地数'+str(self.__field_num)+'_队伍数'+str(self.__team_num)+'.xlsx'
        df.to_excel(self.__fileName)

        # df.to_excel('matchups.xlsx')

if __name__ == '__main__':
    newMatchups=createMatchups(5,7)
    newMatchups.initInfo()
    newMatchups.getAllMatchups()
    newMatchups.export2Excel()