#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     weibo
   Description :
   Author :       zhaojianghua
   date：          2019/1/1
   https://m.weibo.cn/u/2830678474
'''

from urllib.parse import urlencode
import requests,json
import pprint
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url='https://m.weibo.cn/api/container/getIndex?'

headers={
    'Host':'m.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    params={
            'type' : 'uid',
            'value' : '2830678474',
            'containerid' : '1076032830678474',
            'page':page
    }

    url=base_url+urlencode(params)

    try:
        response=requests.get(url,headers=headers)
        if response.status_code ==200:
            return  response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(jsons):
    if jsons:
        items=jsons.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            #print(item)
            if item:
                print('**********************************************************************')
                weibo={}
                weibo['id']=item.get('mid')
                weibo['text']=pq(item.get('text')).text()
                weibo['attitudes']=item.get('attitudes_count')
                weibo['comments']=item.get('comments_count')
                weibo['reposts']=item.get('reposts_count')
                yield weibo

client=MongoClient('mongodb://localhost:27017/')
db=client['weibo']
collection=db['weibo']

def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')

if __name__ == '__main__':
    for page in range(1,11):
        jsons=get_page(page)
        results=parse_page(jsons)
        for result in results:
            print(result)
            save_to_mongo(result)