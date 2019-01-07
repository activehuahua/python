#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : getBooks.py
@Time    : 2019/1/7 15:28
@desc   :
'''

import requests
#from lxml import etree
from pyquery import  PyQuery as pq
from jsonpath import jsonpath
import json

class Spider(object):
    def start_request( self ,bookId):

        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        _csrfToken='2EqV4zyJWPUZPWaMIwYNGZ6lSLhkzu7iWvkDv6zj'
        base_url='https://book.qidian.com/ajax/book/category?'
        url=base_url+_csrfToken+'&bookId='+bookId

        response=requests.get(url,headers=headers)
        py_data = json.loads(response.content.decode())

        data_chapter_name=jsonpath(py_data,'$..cN')
        data_chapter_id=jsonpath(py_data,'$..id')
        for item in range(len(data_chapter_id)):
            data_chapter_id[item]='https://read.qidian.com/chapter/'+str(bookId)+'/'+str(data_chapter_id[item])

        for name, id in zip(data_chapter_name,data_chapter_id):
            print(name,id )

spider=Spider()
spider.start_request('1010734492')
spider.start_request('1004608738')