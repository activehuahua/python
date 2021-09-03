#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : zhihu-explore.py
@Time    : 2018/12/25 18:54
@desc   :
'''

import requests
from pyquery import  PyQuery as pq

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

url='https://www.zhihu.com/explore'

html=requests.get(url,headers=headers).text
doc=pq(html)

items=doc('.ExploreRoundtableCard-questionItem').items()
with open('explore.txt', 'w', encoding='utf-8') as f:
    for item in items:
        question=item.find('.ExploreRoundtableCard-questionTitle').text()
        answer=item.find('.ExploreRoundtableCard-questionCounts span').text()
        # answer=pq(item.find('.ExploreRoundtableCard-questionCounts span').html()).text()

        print(question,answer)

        f.write('\n'.join([question,answer]))
        f.write('\n'+'='*50+'\n')