#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : proxy-ep1.py
@Time    : 2018/12/11 15:23
@desc   :
'''

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
import json
import redis, time

# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'
#带用户名和密码的代理
#proxy='username:password@127.0.0.1:59029'
def print_ip(proxy):
    proxy_handler=ProxyHandler({
        'http':'http://'+proxy
        #'http':proxy
    })

    opener =build_opener(proxy_handler)
    try:
        response = opener.open('http://httpbin.org/get')
        data_json=json.loads(response.read().decode('utf-8'))
            #print(response.read().decode('utf-8'))
        print(data_json['origin'] )
    except URLError as e:
        # print(type(e.reason))
        # print(e.reason)
        pass

def get_redisDB():


    db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
    return db

def get_proxies():
    db=get_redisDB()
    #print(db.zrange(REDIS_KEY, 0, -1,withscores=True))
    proxies=db.zrange(REDIS_KEY, 0, -1)
    return proxies

if __name__ == '__main__':
    proxies=get_proxies()
    for item in proxies:
        print_ip(item)