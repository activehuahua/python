#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : json-ep1.py
@Time    : 2018/12/10 18:10
@desc   :
'''

# from  urllib import  request
import requests
import  json
from bs4 import  BeautifulSoup

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
}

# r=requests.get('http://cc.huimaifang.com/',headers=headers)

# html = request.urlopen(r'https://api.douban.com/v2/book/1220562',headers=headers)
html = requests.get(r'https://api.douban.com/v2/book/1220562',headers=headers)
# hjson = json.loads(html.read())
hjson=json.loads(html.content)

# print(html.text)

# soup=BeautifulSoup(html.read(),'lxml')
# # print(soup)
# # print(hjson['id'])
# # print(hjson['rating']['max'])
# # print(hjson['tags'][0]['name'])
# # print(hjson['publisher'])
# # print(hjson['tags'])

print(hjson['msg'])
print(hjson['code'])
print(hjson['request'])
# #
# # for item in range(len(hjson['tags'])) :
# #     print(hjson['tags'][item])