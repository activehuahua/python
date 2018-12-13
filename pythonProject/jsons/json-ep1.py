#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : json-ep1.py
@Time    : 2018/12/10 18:10
@desc   :
'''

from  urllib import  request
import  json
from bs4 import  BeautifulSoup

html = request.urlopen(r'https://api.douban.com/v2/book/1220562')
hjson = json.loads(html.read())

#print(hjson)
soup=BeautifulSoup(html.read(),'lxml')
print(soup)
print(hjson['id'])
print(hjson['rating']['max'])
print(hjson['tags'][0]['name'])
print(hjson['publisher'])