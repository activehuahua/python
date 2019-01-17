# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 16:41
# @Author  : zhaojianghua
# @File    : redis-ep1.py
# @Software: PyCharm
# @Desc    :
import redis,time

# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

#pool=redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
#db.zadd(REDIS_KEY,100,'122.133.122.45')
#db=redis.Redis(connection_pool=pool)
db.set('name2','junxi',nx=True,px=30000)
print(db.get('name2'))
time.sleep(1)
print(db.get('name2'))


print(db.mget("name","name2"))

r=db

r.set("cn_name", "君惜大大") # 汉字
print(r.getrange("cn_name", 0, 2))   # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("cn_name", 0, -1))  # 取所有的字节 君惜大大 切片操作
r.set("en_name","junxi") # 字母
print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("en_name", 0, -1)) # 取所有的字节 junxi 切片操作

keydict={'k1': 'v1', 'k2': 'v2'}
r.mset(keydict) # 这里k1 和k2 不能带引号 一次设置对个键值对
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
print(r.mget("k1"))

r.zadd(REDIS_KEY, 'm1', 22)