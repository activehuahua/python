#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : singleList.py
@Time    : 2018/12/18 9:17
@desc   :
'''


class Node(object):
    def __init__(self, elem):
        self.item = elem
        self.next = None


class SingleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print('\n')

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def remove(self, item):
        pre = None
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if (cur == self.__head):
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def search(self, item):
        cur = self.__head
        while cur != None:
            if (cur.item == item):
                return True
            else:
                cur = cur.next
        return False

    def reverse(self):
        cur = self.__head
        pre = None
        if (self.is_empty()):
            return None
        while cur != None:
            if cur.next != None:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            else:
                cur.next = pre
                self.__head = cur
                break


    def mid_position(self):
        fast=self.__head
        slow=fast
        pos=0
        while (fast.next!=None and fast.next.next!=None):
            fast= fast.next.next
            slow=slow.next
            pos+=1
        if self.length()%2 ==0:
            pos+=1
        return pos

if __name__ == "__main__":
    # node = Node(100)  # 先创建一个节点传进去

    ll = SingleLinkedList()
    # print(ll.is_empty())
    # print(ll.length())

    for i in range(13):
        ll.append(i)
    ll.travel()
    ll.reverse()
    ll.travel()
    print(ll.mid_position())
