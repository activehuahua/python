#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : lxml-eps.py
@Time    : 2018/12/19 15:10
@desc   :
'''

from lxml import etree
from bs4 import BeautifulSoup

# xml=etree.parse('./books.xml',etree.XMLParser())
# result=xml.xpath('/bookstore/book[price>30]//text()')
# print(result)
#
# result=xml.xpath('/bookstore/book/title[@*]/text()')
# print(result)
#
# result=xml.xpath('/bookstore/book//attribute::*')
# print(result)
#
# result=xml.xpath('/bookstore/book/descendant::*/text()')
# print(result)
#
# result=xml.xpath('/bookstore/book/child::*/text()')
# print(result)
#
# result=xml.xpath('/bookstore/book/following::*/text()')
# print(result)
#
# # result=xml.xpath('/bookstore/book/following-sibling::*')
# print(result)

with open('./books.xml','r') as f:
    xml=f.read()

soup=BeautifulSoup(xml,'lxml')
title_list=soup.find_all(name='title')
print(title_list)
for item in title_list:
    print(item.string,end=',')