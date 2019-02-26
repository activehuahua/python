# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 9:41
# @Author  : zhaojianghua
# @File    : downloadImages.py
# @Software: PyCharm
# @Desc    :

import requests
import json
from lxml import etree

url='https://www.douban.com/j/search_photo?q=%E7%8E%8B%E7%A5%96%E8%B4%A4&limit=20&start=0'

response=requests.get(url)

def download(src, id):
	dir = './img/' + str(id) + '.jpg'
	try:
		pic = requests.get(src, timeout=10)
		fp = open(dir, 'wb')
		fp.write(pic.content)
		fp.close()
	except requests.exceptions.ConnectionError:
		print('图片无法下载')


html=json.loads(response.text,encoding='utf-8')

image_mount=int(html['total'])
print(f'total is {image_mount}')

for image in html['images']:
    src=image['src']
    src=src.replace('thumb', 'l')
    print(src)
    download(src, image['id'])  # 下载一张图片

