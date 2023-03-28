# !/usr/bin/env python3
# -*- coding: utf-8 -*-#

'''
# Name:         dazhuan
# Description:  6人打转
# Author:       alex
# Date:         2023/3/28
'''
import queue
import random

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
        self.__count=0
        '''已有的组合'''
        self.__comboes=[]
        '''队列中的中间list'''
        self.__leftList=[]
        '''队列外元素'''
        self.__rightList=[]
        '''总的局数'''
        self.__totalCount=6
    '''初始化人员，每次出场人数'''
    def setMembers(self,count,member_list):
        self.__members=member_list
        self.__count=count

    def getLeftList(self):
        return self.__leftList

    '''初始化队列'''
    def getInitQueue(self):
        members=self.__members[:]
        # print(self.__members)
        self.__queueLeft=self.getRandom(self.__count,self.__members)
        self.__rightList = list(set(members).difference(set(self.__queueLeft)))
        print(self.__queueLeft,self.__leftList,self.__rightList)

    '''获取对阵'''
    def getMatchups(self):
        # self.getInitQueue()
        randomList=[]
        tempList=[]
        for i in range(self.__totalCount):
            for num in range(2):
                randomList.append(self.__queueLeft[0])
                tempList.append(self.__queueLeft[0])

                self.__queueLeft.pop(0)

            # print(self.__queueLeft,len(self.__queueLeft))
            self.__comboes.append(randomList)
            self.__comboes.append(self.__queueLeft)

            for index in range(len(self.__rightList)):
                self.__queueLeft.append(self.__rightList[index])
            print('self.__queueLeft:%s'%self.__queueLeft)
            # print(self.__rightList)
            self.__rightList.clear()
            self.__rightList=tempList
            print(self.__rightList)
            randomList = []
            tempList=[]
            print(self.__comboes)
        # print(self.__comboes)




    '''从list中随机抽取count个随时元素'''
    def getRandom(self,count,sourceList):
        randomList=[]
        templist=sourceList[:]
        while len(randomList)<count:
            index=random.randint(0,len(templist)-1)
            randomList.append(templist[index])
            templist.pop(index)
        # randomList.sort()
        self.__rightList=templist
        return randomList


if __name__ == '__main__':
    dazhuan= DaZhuan()
    sourceList=['1','2','3','4','5','6']
    dazhuan.setMembers(4,sourceList)
    # list1=dazhuan.getRandom(4,sourceList)
    # list2=dazhuan.getLeftList()
    # print(list1)
    #
    # print(list2)
    dazhuan.getInitQueue()
    dazhuan.getMatchups()





