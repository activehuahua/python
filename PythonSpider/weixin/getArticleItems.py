# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 16:45
# @Author  : zhaojianghua
# @File    : getArticleItems.py
# @Software: PyCharm
# @Desc    :

import requests
from pyquery import PyQuery as pq
from weixin.config import *
from weixin.redisDB import RedisQueue
from weixin.mongoDB import MONGO
import  re

url='https://mp.weixin.qq.com/s?src=11&timestamp=1548377038&ver=1387&signature=TM3vsMhJGJ1O1*ak-ggPqIMTy5SFlDI0cKUAdqfR6xoOkoHhFpvCsE7SyJvtIjjrV3HFH22mnR54*v0*qVfI2YTKF47yvv5YoJmmtiIjih-zLKnRIfqSExtmO8YczGK3&new=1'



def parse_detail(response):
    """
    解析详情页
    :param response: 响应
    :return: 微信公众号文章
    """
    html=response.content.decode()
    #html='    var publish_time = "2018-11-22" || "";'
    #print(html)
    doc = pq(html)
    print(doc)
  #  print(html)
 #   print(doc)
    result= re.search(r'var publish_time = "(.*?)"', html, re.M | re.I )

    date=result.group(1)
    data = {
        'title': doc('.rich_media_title').text(),
        'content': doc('.rich_media_content').html(),
       # 'date': doc('#post-date').text(),
        'date':date,
        'author': doc('#meta_content .rich_media_meta.rich_media_meta_text').text(),
        'wechat': doc('#js_name').text()
    }
    yield data

if __name__ == '__main__':
    response = requests.get(url)
    result=parse_detail(response)
 #   print(result)
    mongo=MONGO()
    for item in result:
        print(item)
        mongo.save_to_mongo('articles',item)
