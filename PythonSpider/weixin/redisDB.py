from  redis import StrictRedis
from  weixin.config import *
from  pickle import dumps, loads
from  weixin.request import WeixinRequest


class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self,redis_key, request):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :param fail_time: 失败次数
        :return: 添加结果
        """
        if isinstance(request, WeixinRequest):
            return self.db.rpush(redis_key, dumps(request))
        return False

    def pop(self,redis_key):
        """
        取出下一个Request并反序列化
        :return: Request or None
        """
        if self.db.llen(redis_key):
            return loads(self.db.lpop(redis_key))
        else:
            return False

    def clear(self,redis_key):
        self.db.delete(redis_key)

    def empty(self,redis_key):
        return self.db.llen(redis_key) == 0


if __name__ == '__main__':
    db = RedisQueue()
    start_url = 'http://www.baidu.com'
    weixin_request = WeixinRequest(url=start_url, callback='hello', need_proxy=True)
    db.add(weixin_request)
    request = db.pop()
    print(request)
    print(request.callback, request.need_proxy)
