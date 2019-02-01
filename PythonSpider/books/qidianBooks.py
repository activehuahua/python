# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 15:31
# @Author  : zhaojianghua
# @File    : qidianBooks.py
# @Software: PyCharm
# @Desc    :


import requests
from lxml import etree
import os


class Spider(object):
    def start_request(self):
        # 1. 请求一级页面数据，抽取小说名创建文件夹，抽取二级页面链接
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.text)
        Bigtit_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        Bigsrc_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')

        for BigTit, Bigsrc in zip(Bigtit_list, Bigsrc_list):
            if os.path.exists(BigTit) == False:
                os.mkdir(BigTit)
            self.file_data(BigTit, Bigsrc)

    def file_data(self, BigTit, Bigsrc):
        # 2. 请求二级页面数据，抽取每章名，抽取三级页面链接
        response = requests.get("http:" + Bigsrc)
        html = etree.HTML(response.text)
        Littit_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        Litsrc_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        for Litsrc, Littit in zip(Litsrc_list, Littit_list):
            # print(Littit,Litsrc)
            self.finally_file(Littit, Litsrc, BigTit)

    def finally_file(self, Littit, Litsrc, Bigtit):
        # 3. 请求三级页面，抽取文章内容，写入文件并保存到小说文件夹
        response = requests.get("http:" + Litsrc)
        html = etree.HTML(response.text)
        content = "\n".join(html.xpath('//div[@class="read-content j_readContent"]/p/text()'))  #将列表转化成字符串
        file_name = Bigtit + "\\" + Littit + ".txt"
        print("正在存储文件：" + file_name)
        with open(file_name,"a",encoding="utf-8") as f:
            f.write(content)


spider = Spider()
spider.start_request()
