from requests import Session
from weixin.config import *
from weixin.redisDB import RedisQueue
from weixin.mongoDB import MONGO
from weixin.request import WeixinRequest
from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError
import  re

class Spider():
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = 'NBA'
    proxy = {
        "http": "http://" + PROXY_ip_port,
        "https": "https://" + PROXY_ip_port
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'SNUID=3C20585A7772F86EA3D34268786AE214;SUV=00293A697D4600BF5C35B5C076C91335;',
        'Host': 'weixin.sogou.com',
        'Referer': 'http://weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'Proxy-Authorization': 'Basic ' + PROXY_appKey,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    #cookies=None
    session = Session()
    queue = RedisQueue()
    queue_article=RedisQueue()
    mongo = MONGO()



    def start(self):
        """
        初始化工作
        """
        # 全局更新Headers
        self.queue_article.clear(REDIS_KEY_ARTICLE)
        self.queue.clear(REDIS_KEY)
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, headers=self.headers,need_proxy=True)
        # 调度第一个请求

        self.queue.add(REDIS_KEY ,weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """

        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request_article = WeixinRequest(url=url, headers=self.headers,need_proxy=True)
            self.queue_article.add(REDIS_KEY_ARTICLE,weixin_request_article)
            #yield weixin_request_article
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, headers=self.headers,need_proxy=True)
            yield weixin_request
            self.queue.add(REDIS_KEY,weixin_request)

    def selfPrint(self):

        print('*' * 50)


    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        """

        html = response.content.decode()
        try:
            result = re.search(r'var publish_time = "(.*?)"', html, re.M | re.I)
            date = result.group(1)
        except Exception as e:
            pass
        finally:
            date=None

        doc = pq(html)
        # data = {
        #     'title': doc('.rich_media_title').text(),
        #     'content': doc('.rich_media_content').text(),
        #     'date': doc('#publish_time').text(),
        #     # 'nickname': doc('#js_profile_qrcode > div > strong').text(),
        #     # 'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        #     'author':doc('#js_author_name').text(),
        #     'wechat':doc('#js_profile_qrcode .profile_meta .profile_meta_value').text()
        # }
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').html(),
            # 'date': doc('#post-date').text(),
            'date': date,
            'author': doc('#meta_content .rich_media_meta.rich_media_meta_text').text(),
            'wechat': doc('#js_name').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
           # if weixin_request.need_proxy:

                # return self.session.send(weixin_request.prepare(),
                #                              timeout=weixin_request.timeout, allow_redirects=False, proxies=self.proxy)
             url=weixin_request.url
             return self.session.get(weixin_request.url,headers=self.headers,proxies=self.proxy, verify=False, allow_redirects=False )
            #return self.session.get(weixin_request.url, headers=self.headers)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request Failed', weixin_request.fail_time, 'Times ', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(REDIS_KEY ,weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty(REDIS_KEY):
            weixin_request = self.queue.pop(REDIS_KEY)
            # callback = weixin_request.callback

            print('Schedule', weixin_request.url)
            #response = self.request(weixin_request)
            #response=requests.get(weixin_request.url,headers=self.headers,proxies=self.proxy, verify=False, allow_redirects=False)
            response = self.session.get(weixin_request.url, headers=self.headers)
            # self.cookies=response.cookies
            # print(self.cookies)


            if response and response.status_code in VALID_STATUSES:
                #results = list(callback(response))

                self.parse_index(response)

                while not self.queue_article.empty(REDIS_KEY_ARTICLE):
                    weixin_request_artile=self.queue_article.pop(REDIS_KEY_ARTICLE)

                    #response_article=self.session.get(weixin_request_artile.url, headers=self.headers)
                    #url='http://mp.weixin.qq.com/s?src=11&timestamp=1548387724&ver=1387&signature=0rFktbtZaY7FzRblX7xkTwqMryiLqiqmiSp8iFxqkci3tAQkk9qnwjSRFx22k8bWmOpNfGV61K-JlekaGfqF-iATCR1uxwqcaojXax9*zEWsclkNa3r7DXhXI96z-iSf&new=1'
                    #response_article = self.session.get( url, headers=self.headers)
                    response_article = requests.get(weixin_request_artile.url)
                    results=self.parse_detail(response_article)

                    if results:
                        for result in results:
                            print('New Result', type(result))
                            # if isinstance(result, WeixinRequest):
                            #     self.queue.add(result)
                            if isinstance(result, dict):
                                self.mongo.save_to_mongo('articles', result)
            elif  response.status_code ==302 or response.status_code==301:
                    loc=response.headers['Location']
                    url=weixin_request.url+loc
                    response = self.session.get(url, headers=self.headers)
                    self.parse_index(response)
                    while not self.queue_article.empty(REDIS_KEY_ARTICLE):
                        weixin_request_artile = self.queue_article.pop(REDIS_KEY_ARTICLE)
                        response_article = self.session.get(weixin_request_artile.url, headers=self.headers)
                        results = self.parse_detail(response_article)
                        if results:
                            for result in results:
                                print('New Result', type(result))
                                # if isinstance(result, WeixinRequest):
                                #     self.queue.add(result)
                                if isinstance(result, dict):
                                    self.mongo.save_to_mongo('articles', result)

            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()

