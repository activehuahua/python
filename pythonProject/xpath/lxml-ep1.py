#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : lxml-ep1.py
@Time    : 2018/12/18 18:25
@desc   :
'''

from lxml import etree

text='''
<div><ul>
<li class='item-0'><a href="link1.html"> first item</a></li>
<li class='item-1'><a href="link1.html"> second item</a>
</ul>
'''
# html=etree.HTML(text)
# result=etree.tostring(html)
# print(result.decode('UTF-8'))
# with open('test.html','w') as f:
#     f.write(result.decode('UTF-8'))

html=etree.parse('test.html',etree.HTMLParser())
result=html.xpath('//li//a')
print(result)