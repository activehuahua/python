# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 14:52
# @Author  : zhaojianghua
# @File    : script.py
# @Software: PyCharm
# @Desc    :

import json
import pymongo
from mitmproxy import ctx

#client = pymongo.MongoClient('localhost')
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# db = client.igetget
# collection = db.books

def response(flow):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.igetget
    collection = db.books
    #url = 'https://dedao.igetget.com/v3/discover/bookList'
    url = 'https://entree.igetget.com/ebook2/v1/ebook/list'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title': book.get('operating_title'),
                'cover': book.get('cover'),
                'summary': book.get('other_share_summary'),
                'price': book.get('price')
            }
            ctx.log.info(str(data))
            collection.insert(data)