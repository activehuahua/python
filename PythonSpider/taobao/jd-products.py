# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:59
# @Author  : zhaojianghua
# @File    : jd-products.py
# @Software: PyCharm
# @Desc    : 抓取京东商品列表

import requests
from pyquery import PyQuery as pq
from urllib.parse import quote
import re
import json
import pymongo

KEYWORD='iPad'
url='https://search.jd.com/Search?keyword=iPad'
comment_url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds='
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}

def get_products():
    response=requests.get(url,headers=headers)

    doc = pq(response.content.decode())
    #获取商品列表标签对应items
    items = doc('#J_goodsList .gl-warp .gl-item').items()
    #print(items)

    for item in items:
        #item为pyquery类型
        #print(type(item))

        #使用re时候必须转换类型为str
        item1=str(item)
        pattern=re.compile(r'<li data-sku="(\d+)"',re.S)
        result=re.match(pattern,item1)
        product_id=int(result.group(1))

        #调用接口返回json数据
        comment_response=requests.get(comment_url+str(product_id))
        comment_json=json.loads(comment_response.text)

        #获取对应的评论数，json返回一个值，用0定位，再获取对应key的值
        comment_count=comment_json['CommentsCount'][0]['CommentCountStr']

        # 每个商品放入product字典
        product = {
            'id':product_id,
            # 对应的需要从item中打印获取到具体的attr值
            'image': 'http:'+item.find('.p-img img').attr('source-data-lazy-img'),
            'price': item.find('.p-price').text(),
            'comment': comment_count,
            'title': item.find('.p-name a em').text(),
            'shop': item.find('.p-shop .J_im_icon a').text()
        }

        # 将所有商品纳入迭代器中
        yield product
    return product

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.taobao  #数据库名
collection = db.products  #相当于关系型数据库的数据表

def save_to_mongo(result):
    try:
        #所有商品一次性插入mongoDB
        if collection.insert_many(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

if __name__ == '__main__':
    products=get_products()
    save_to_mongo(products)
