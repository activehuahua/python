#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     singleLinkedList
   Description :
   Author :       Administrator
   date：          2018/12/17
'''


class Node(object):
    def __init__(self, elem):
        self.item = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while (cur != None):
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while (cur != None):
            print(cur.item, end=' ')
            cur = cur.next
        print('\n')

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node=Node(item)
        if (self.is_empty()):
            self.__head=node
        else:
            cur=self.__head
            while (cur.next!= None):
                cur=cur.next
            cur.next=node

    def insert(self, pos, item):
        if(pos<=0):
            self.add(item)
        elif (pos>=self.length()):
            self.append(item)
        else:
            node=Node(item)
            count=0
            cur=self.__head
            while count<pos-1:
                count+=1
                cur=cur.next

            node.next=cur.next
            cur.next = node

    def remove(self, item):
        cur=self.__head
        pre=None
        while cur!=None:
            if (cur.item==item):
                if(cur==self.__head):
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next


    def search(self, item):
        cur=self.__head
        while cur != None:
            if(cur.item==item):
                return True
            else:
                cur=cur.next
        return False

if __name__=="__main__":
    singleList=SingleLinkList()
    print('Length is %s'% singleList.length())
    singleList.add(1)

    singleList.travel()
    singleList.add(10)
    singleList.travel()
    singleList.add(100)
    singleList.travel()
    singleList.append(200)
    singleList.travel()
    singleList.insert(2,50)
    singleList.travel()
    singleList.remove(50)
    singleList.travel()
    print(singleList.search(200))
    singleList.insert(-2,2)
    singleList.travel()