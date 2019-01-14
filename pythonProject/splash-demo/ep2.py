# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 14:49
# @Author  : zhaojianghua
# @File    : ep2.py
# @Software: PyCharm
# @Desc    :

import scrapy
from scrapy_splash import SplashRequest


class TbtaobaoSpider(scrapy.Spider):
    name = "tbtaobao"
    allowed_domains = ["www.taobao.com"]
    start_urls = ['https://s.taobao.com/search?q=坚果&s=880&sort=sale-desc']

    def start_requests(self):
        for url in self.start_urls:
            # yield Request(url,dont_filter=True)
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print(response.text)