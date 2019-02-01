import pymongo

REDIS_HOST = 'localhost'

REDIS_PORT = 6379

REDIS_PASSWORD = None

REDIS_KEY = 'weixin'

REDIS_KEY_ARTICLE = 'weixin_article'

PROXY_POOL_URL = 'http://127.0.0.1:5555/random'

PROXY_appKey = "cE9KZWZoOGJaV0NEWlAzRzpUYnpsNkNzaTl4TloxdkEw"

# 蘑菇隧道代理服务器地址
PROXY_ip_port = 'transfer.mogumiao.com:9001'

#MongoDB
#CLIENT = pymongo.MongoClient('mongodb://localhost:27017/')
MONGO_URL='mongodb://localhost:27017/'
#MONGO_DB = CLIENT.weixin  #数据库名

#COLLECTION = MONGO_DB.articles  #相当于关系型数据库的数据表

TIMEOUT = 10

MAX_FAILED_TIME = 1

VALID_STATUSES = [200]

# MYSQL_HOST = 'localhost'
#
# MYSQL_PORT = 3306
#
# MYSQL_USER = 'root'
#
# MYSQL_PASSWORD = '123456'
#
# MYSQL_DATABASE = 'weixin'