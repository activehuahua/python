# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 14:13
# @Author  : zhaojianghua
# @File    : get-lists.py
# @Software: PyCharm
# @Desc    :抓取淘宝列表页

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
import time

browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
KEYWORD='iPad'

def index_page(page):
    """
    抓取索引页
    :return:
    """
    print("正在抓取第",page,"页")
    try:
        url='https://search.jd.com/Search?keyword='+quote(KEYWORD)
        browser.get(url)
        # if page >1:
        #     input=wait.until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR,'.input-txt'))
        #     )
        #     submit=wait.until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn btn-default'))
        #     )
        #     input.clear()
        #     input.send_keys(page)
        #     submit.click()
        # wait.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.curr'),str(page)))
        # print('find page number')
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_goodsList .gl-warp clearfix li ')))
        time.sleep(3)
        get_products()
    except TimeoutException:
        print('Time out!')

def get_products():
    """
    提取商品数据
    :return:
    """
    html=browser.page_source
    doc=pq(html)
    items=doc('#J_goodsList .gl-warp .gl-item').items()
    #print(items)
    for item in items:
        #print(item)
        image=item.find('.p-img img').attr('src')
        print(image)
        product={
            'image':item.find('.p-img img').attr('src'),
            'price':item.find('.p-price').text(),
            'comment':item.find('.p-commit strong a').text(),
            'title':item.find('.p-name a em').text(),
            'shop':item.find('.p-shop .J_im_icon a').text()
        }
        print(product)
        #save_to_mongo(product)


client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.taobao  #数据库名
collection = db.products  #相当于关系型数据库的数据表

def save_to_mongo(result):
    try:
        if collection.insertMany(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

if __name__ == '__main__':
    index_page(1)