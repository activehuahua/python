#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : pyquery-ep1.py
@Time    : 2018/12/25 16:28
@desc   :
'''
html='''
<html><body><div id="container"><ul class="list">
<li class="item-0 active"><a href="link1.html"> first item</a></li>
<li class="item-1"><a href="link2.html"> second item</a></li>
<li class="item-inactive"><a href="link3.html"> <span class="bold">third item</span></a></li>
<li class="item-1"><a href="link4.html"> fourth item</a></li>
<li class="item-0"><a href="link5.html"> fifth item</a>
</li></ul>
</div></body></html>
'''

from pyquery import PyQuery as pq
import  requests

# doc=pq(html)
# print(doc('li'))
#
# doc=pq(url='https://cuiqingcai.com')
# print(doc('title'))

# doc=pq(requests.get('https://cuiqingcai.com').text)
# print(doc('title'))

# doc=pq(html)
# print(doc('#container .list li'))

# doc=pq(html)
# items=doc('.list')
# print(items)
#
# lis=items.find('li')
# print(lis)

doc=pq(html)
print(doc('.bold').text())

a=doc('.item-0.active a')
print(a.attr('href'))
print(a.attr.href)

a=doc('a')
for item in a.items():
    print(item.attr.href)