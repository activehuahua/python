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
        self.__count=4
        '''已有的组合[['1','2','3','4'], ['2','3','5','6']] 每组选手前2位为队友，后2位为队友，组合list共有6组元素'''
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
        print(self.__queueLeft,self.__rightList)

    '''获取对阵'''
    def getMatchups(self):
        self.getInitQueue()
        randomList=[]
        tempList=[]
        comblist=[]
        # memberResult = False
        rightList=self.__rightList[:]
        comboes=self.__comboes[:]
        # for i in range(self.__totalCount):
        while(len(self.__comboes)<6):
            result=False

            '''从queueLeft中4个中随机2个进组合，判断已有组合中是否存在'''
            while(not result):

                comblist=self.getRandom(2,self.__queueLeft)
                set_comblist = set(comblist)
                set_queueList = set(self.__queueLeft)
                tempList = list(set_queueList.difference(set_comblist))
                print('comblist:%s,tempList:%s,queueLeft:%s'%(comblist,tempList,self.__queueLeft))

                memberResult1=False
                memberResult2=False
                for index in range(len(comblist)):
                    # memberResult1 = False
                    memberResult1 =self.is_more_than_twice(self.__comboes, comblist[index])
                    if memberResult1:
                        self.removeMemberFromQueueList(comblist[index])
                        continue

                for index in range(len(tempList)):
                    # memberResult2 = False
                    memberResult2 = self.is_more_than_twice(self.__comboes, tempList[index])
                    if memberResult2:
                        self.removeMemberFromQueueList(tempList[index])
                        continue
                if (memberResult2 or memberResult1):
                    continue
                elif  not self.compareDiffert(self.__comboes,comblist) and not self.compareDiffert(self.__comboes,tempList):

                    # if ( not memberResult):
                        result = True
                        middleList=[]
                        middleList.append(comblist)
                        middleList.append(tempList)

                        self.__comboes.append(middleList)
                        print('comblist:%s'%comblist)
                        self.removeMemberFromList(comblist)
                        # print(len(self.__rightList))
                        print('queueList1:%s'%self.__queueLeft)
                        self.__queueLeft.extend(self.__rightList)
                        print('queueList2:%s' % self.__queueLeft)
                        self.__rightList.clear()
                        self.__rightList.extend(comblist)
                        comblist=[]
                        tempList = []
                        print('comboes:%s' % self.__comboes)
                        print('----------------------------------------------------')

            randomList = []
            tempList=[]

        # print('comboes:%s' % comboes)

    def removeMemberFromQueueList(self,member):
        print('queus原始%s'%self.__queueLeft)
        self.__queueLeft.remove(member)
        self.__rightList.extend(member)

        temp=self.__rightList[0]
        print('temp:%s'%temp)
        self.__rightList.pop(0)
        self.__queueLeft.extend(temp)
        print('member:%s,queueList:%s'%(member,self.__queueLeft))

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
        # for element in memberList:
        #     if element in source:
        #         source.remove(element)
        # return source
        set1=set(self.__queueLeft)
        set2=set(memberList)
        tempList=list(set1.difference(set2))
        self.__queueLeft=tempList
        # return tempList



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


if __name__ == '__main__':
    dazhuan= DaZhuan()
    sourceList=['1','2','3','4','5','6']
    dazhuan.setMembers(4,sourceList)
    dazhuan.getMatchups()
