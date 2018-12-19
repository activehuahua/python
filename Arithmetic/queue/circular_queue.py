#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     circular_queue.py
   Description :
   Author :       zhaojianghua
   date：          2018/12/19
'''
from arithmetic.linkedList.singleLinkedList import Node
from typing import Optional
from itertools import chain

class CirularQueue():
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity+1
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self):
        if (self._head == self._tail):
            return
        ret = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return ret

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head : self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))

if __name__ == "__main__":
    queue = CirularQueue(5)
    for i in range(5):
        queue.enqueue(str(i))
    queue.enqueue(8)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue('8')
    queue.dequeue()
    print(queue)
