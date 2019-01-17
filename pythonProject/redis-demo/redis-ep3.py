# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 17:20
# @Author  : zhaojianghua
# @File    : redis-ep3.py
# @Software: PyCharm
# @Desc    :

import redis,time

# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies-1'

db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

ip_set={'122.133.122.45:8080':10}

# 有序集合
db.zadd(REDIS_KEY,ip_set)

#有序集合的某个具体key值减1   name, amount,value
#db.zincrby(REDIS_KEY, -1, '122.133.122.45:8080' )
for item in db.zrange(REDIS_KEY,0,-1):
    print(item)
    db.zincrby(REDIS_KEY, -2, item )
#db.zrem(REDIS_KEY, '122.133.122.45:8080')

print(db.zrange(REDIS_KEY,0,-1,withscores=True))