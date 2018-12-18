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

    def getHead(self):
        return self.__head

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

    def remove_pos_node(self, pos):
        pre = None
        cur = self.__head
        count = 0
        while cur != None:
            if count == pos:
                if (cur == self.__head):
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
                count += 1

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
        fast = self.__head
        slow = fast
        pos = 0
        while (fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
            pos += 1
        if self.length() % 2 == 0:
            pos += 1
        return pos

    def is_circle(self):
        pass


def mergeTwoSortedLinkedList(list1, list2):
    cur1 = list1.getHead()
    cur2 = list2.getHead()
    list = SingleLinkedList()
    while cur1 != None and cur2 != None:
        if (cur1.item > cur2.item):
            list.append(cur2.item)
            cur2 = cur2.next
        else:
            list.append(cur1.item)
            cur1 = cur1.next
    if cur1 != None:
        while  cur1.next != None:
            list1.append(cur1.item)
            cur1 = cur1.next
        list.append(cur1.item)
    if cur2 != None:
        while cur2.next != None:
             list.append(cur2.item)
             cur2 = cur2.next
        list.append(cur2.item)
    return list


if __name__ == "__main__":
    # node = Node(100)  # 先创建一个节点传进去

    ll = SingleLinkedList()
    print(ll.is_empty())
    print(ll.length())

    for i in range(13):
        ll.append(i)
    ll.travel()
    # ll.reverse()
    # ll.travel()
    # print(ll.mid_position())
    # ll.remove_pos_node(6)
    # ll.travel()

    list1 = SingleLinkedList()
    list2 = SingleLinkedList()

    for i in range(0,5):
        list1.append(i)
    print(list1.length())
    list1.travel()
    for j in range(0, 10, 2):
        list2.append(j)
    list2.travel()
    list=mergeTwoSortedLinkedList(list1, list2)
    list.travel()
