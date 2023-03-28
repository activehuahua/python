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
        self.__totalCount=5
    '''初始化人员，每次出场人数'''
    def setMembers(self,count,member_list):
        self.__members=member_list
        self.__count=count

    def getLeftList(self):
        return self.__leftList

    '''初始化队列'''
    def getInitQueue(self):
        members=self.__members[:]
        self.__queueLeft=self.getRandom(self.__count,self.__members)
        self.__rightList = list(set(members).difference(set(self.__queueLeft)))
        print(self.__queueLeft,self.__leftList,self.__rightList)

    '''获取对阵'''
    def getMatchups(self):
        # self.getInitQueue()
        randomList=[]
        tempList=[]
        queueLeft=self.__queueLeft[:]
        rightList=self.__rightList[:]
        comboes=self.__comboes[:]
        for i in range(self.__totalCount):
            for num in range(2):
                randomList.append(queueLeft[0])
                tempList.append(queueLeft[0])

                queueLeft.pop(0)

            comboes.append(randomList)
            comboes.append(queueLeft)
            print('comboes:%s' % comboes)

            for index in range(len(rightList)):
                queueLeft.append(rightList[index])

            rightList=[]
            # rightList=tempList
            for index in range(len(tempList)):
                rightList.append(tempList[index])

            randomList = []
            tempList=[]

        print('comboes:%s' % comboes)

    '''组合不重复，可以插入'''
    def compareDiffert(list1,list2):
        for i in range(len(list1)):
            if isinstance(list1[i], list):
                list1[i].sort()
                for index1 in range(len(list1[i])):
                    if list1[i][index1] != list2[index1]:
                        print('不存在')
                        return True

                return False


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





