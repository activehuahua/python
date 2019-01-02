#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : lxml-ep2.py
@Time    : 2018/12/19 14:35
@desc   :
'''

from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)

