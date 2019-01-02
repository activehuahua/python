#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : jiepai.py
@Time    : 2019/1/2 10:45
@desc   :
街拍网址： https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D
'''

import requests
from urllib.parse import urlencode
import  pprint,os
from hashlib import md5
from multiprocessing import  Pool

def get_page(offset):
    params={
        'offset' :offset,
        'format' : 'json',
        'keyword' :'街拍',
        'autoload' : 'true',
        'count' :20 ,
        'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code ==200:
            return  response.json()
    except requests.ConnectionError :
        return  None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title= item.get('title')
            images=item.get('image_list')
            if images:
                for image in images :
                        yield{
                            'image' : 'http:'+image.get('url'),
                            'title':title
                        }

def save_image(item):
    dir= os.path.join(os.getcwd()+'/img/'+item.get('title'))
    print(dir)

    try:
        if not os.path.exists(dir) :
            os.makedirs(dir)
        response =requests.get(item.get('image'))

        if response.status_code == 200 :
            file_path ='{0}/{1}.{2}'.format(dir,md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f :
                    f.write(response.content)
            else :
                print('Already Download ',file_path)
    except requests.ConnectionError:
        print('Failed to save Image')
    except Exception :
        pass


def main(offset):
    json=get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START =1
GROUP_END=20

if __name__ == '__main__':
    pool=Pool()
    groups =([x * 20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()

