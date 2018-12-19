#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : bs=ep2.py
@Time    : 2018/12/19 16:28
@desc   :
'''

html ='''
<html><head><title>The Dormouse's story</title></head>
<body>
<!--<p class="title" name="dromouse"<b>The Dormouse's story</b>-->
<p class="story"> Once Upon a time, there were three little sisters; and their names were .
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class ="story">...</p>
'''

from bs4 import BeautifulSoup

soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title.string)
#
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)
#
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
#
#
# print(soup.head.title)
# print(soup.head.title.string)
#
# print(soup.p.contents)
#
# print(soup.p.children)
#
# for i,child in enumerate(soup.p.children):
#     print(i,child)

print(list(enumerate(soup.p.parents)))