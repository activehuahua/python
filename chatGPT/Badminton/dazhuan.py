# !/usr/bin/env python3
# -*- coding: utf-8 -*-#

'''
# Name:         dazhuan
# Description:  6人打转
# Author:       alex
# Date:         2023/3/28
'''
import datetime
import os
import queue
import random
import pandas as pd
from datetime import date

class DaZhuan:
    def __init__(self):
        '''打转人数'''
        self.__members=[]
        '''所有对阵，6局'''
        self.__matchups=[]
        '''工作队列'''
        self.__queueLeft=[]
        '''临时队列'''
        self.__queueRight=[]
        '''每局对阵人数'''
        self.__count=4
        '''已有的组合[['1','2','3','4'], ['2','3','5','6']] 每组选手前2位为队友，后2位为队友，组合list共有6组元素'''
        self.__comboes=[]
        '''队列中的中间list'''
        self.__leftList=[]
        '''队列外元素'''
        self.__rightList=[]
        '''总的局数'''
        self.__totalCount=6

        self.__fileName=''
        self.__roundNames=[]
        self.__field_name=['左场地','右场地']
    '''初始化人员，每次出场人数'''
    def setMembers(self,count,member_list):
        self.__members=member_list
        self.__count=count

    def getLeftList(self):
        return self.__leftList

    def getQueueLeft(self):
        return self.__queueLeft

    def setCombs(self,source):
        self.__comboes=source

    def setRightList(self,source):
        self.__rightList=source

    def setQueue(self, source):
        self.__queueLeft = source

    '''初始化队列'''
    def getInitQueue(self):
        members=self.__members
        self.__queueLeft=self.getRandom(self.__count,self.__members)
        self.__rightList = list(set(members).difference(set(self.__queueLeft)))

        resultPath = os.getcwd() + os.path.sep + 'result'
        if os.path.exists(resultPath):
            print('已存在该文件夹')
        else:
            os.mkdir(resultPath)
        self.__fileName=resultPath+os.path.sep+'打转对阵表_'+str(datetime.datetime.now().date())+'.xlsx'


    '''获取对阵'''
    def getMatchups(self):
        self.getInitQueue()
        randomList=[]
        tempList=[]
        comblist=[]
        rightList=self.__rightList
        comboes=self.__comboes
        roundNum=0
        while(len(self.__comboes)<6):
            result=False
            roundNum+=1
            self.__roundNames.append('第'+str(roundNum)+'局')
            '''从queueLeft中4个中随机2个进组合，判断已有组合中是否存在'''
            while(not result):
                '''清理队列中连打超过2次的元素'''
                for index in range(len(self.__queueLeft)):
                    isMoreThan2=self.is_more_than_twice(self.__comboes,self.__queueLeft[index])
                    if isMoreThan2:
                        self.removeMemberFromQueueList(self.__queueLeft[index])
                comblist=self.getRandom(2,self.__queueLeft)
                set_comblist = set(comblist)
                set_queueList = set(self.__queueLeft)
                tempList = list(set_queueList.difference(set_comblist))

                if not self.compareDiffert(self.__comboes,comblist) and not self.compareDiffert(self.__comboes,tempList):

                        result = True
                        middleList=[]
                        middleList.append(comblist)
                        middleList.append(tempList)

                        self.__comboes.append(middleList)

                        self.removeMemberFromList(comblist)

                        self.__queueLeft.extend(self.__rightList)

                        self.__rightList.clear()
                        self.__rightList.extend(comblist)
                        comblist=[]
                        tempList = []
                        print('comboes:%s' % self.__comboes)

            randomList = []

        print('comboes:%s' % self.__comboes)

    '''将元素从list中删除，添加新元素'''
    def removeMemberFromQueueList(self,member):
        self.__queueLeft.remove(member)
        '''此处会将2个字符的汉字加入list中会只添加单个汉字'''
        # self.__rightList.extend(member)
        self.__rightList.append(member)

        temp=self.__rightList[0]
        self.__rightList.pop(0)
        self.__queueLeft.append(temp)

    '''组合不重复，返回False则对阵list中可以插入'''
    def compareDiffert(self,list1,list2):
        result=False
        set2=set(list2)
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                set1=set(list1[i][j])
                if set1==set2:
                    return True
        return False
    '''判断2个list是否一样元素'''
    def is_same_list(self,list1, list2):
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    '''判断1个人是否连打2局,True代表已经打满2局'''
    def is_more_than_twice(self,source,singleMember):
        lidaCount=0
        countNum=0
        tempList=[]
        for i in range(len(source)-1,-1,-1):
            tempList = []
            countNum = countNum + 1
            for sublist2 in source[i]:
                tempList=tempList+sublist2
            if singleMember in tempList:
                lidaCount=lidaCount+1
                if (countNum==2 and lidaCount==2):
                    return True
            else:
                return False
        return False


    '''从list中移除另外一个list'''
    def removeMemberFromList(self,memberList):
        set1=set(self.__queueLeft)
        set2=set(memberList)
        tempList=list(set1.difference(set2))
        self.__queueLeft=tempList

    def addMemberFromList(self):
        self.__queueLeft.extend(self.__rightList)

    '''从list中随机抽取count个随时元素'''
    def getRandom(self,count,sourceList):
        randomList=[]
        templist=sourceList
        if (len(sourceList)>4):
            print("error len")
        randomList=random.sample(templist,count)
        return randomList

    def export2Excel(self):
        df = pd.DataFrame(columns=self.__field_name, index=self.__roundNames)
        for round_index, round_name in enumerate(self.__roundNames):
            for field_index, field_name in enumerate(self.__field_name):
                df.at[round_name, field_name] = self.__comboes[round_index][field_index]
        df.to_excel(self.__fileName)

if __name__ == '__main__':
    dazhuan= DaZhuan()
    sourceList=["华哥","老虎","暗地","泡泡","炮哥","笨笨"]
    dazhuan.setMembers(4,sourceList)
    dazhuan.getMatchups()
    dazhuan.export2Excel()