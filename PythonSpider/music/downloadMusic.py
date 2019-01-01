#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     downloadMusic
   Description :
   Author :       zhaojianghua
   date：          2018/12/31

   http://music.taihe.com/song/74141979
'''

import requests
import re
from pyquery import PyQuery as pq
import json
#from lxml import etree
import pprint  # 美化打印
def get_music(songid):
    response = requests.get(
        f'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid={songid}&from=web')
    response.encoding = response.apparent_encoding

    data_json = response.json()
    # pprint.pprint(data_json)
    music_url = data_json['bitrate']['file_link']
    music_name = data_json['songinfo']['title']

    print(music_name,music_url)

    music_response = requests.get(music_url)
    with open('MP4/'+music_name+'.mp4','wb') as f :
        f.write(music_response.content)
        print(music_name, '下载完成!')

    #获取一个网页的所有音乐
def get_onePage_music():
    #http://music.taihe.com/search?key=%E5%91%A8%E6%9D%B0%E4%BC%A6
    #response=requests.get('http://music.taihe.com/search?key=%E8%B0%A2%E6%98%A5%E8%8A%B1')
    response=requests.get('http://music.taihe.com/search?key=%E5%91%A8%E6%9D%B0%E4%BC%A6')
    response.encoding = response.apparent_encoding
    #print(response.text)

    songids= re.findall('a href="/song/(\d+)"',response.text)
    print(set(songids))
    for songid in set(songids):
        get_music(songid)

def get_onePage_vip_music():
    #http://music.taihe.com/search?key=%E5%91%A8%E6%9D%B0%E4%BC%A6
    #response=requests.get('http://music.taihe.com/search?key=%E8%B0%A2%E6%98%A5%E8%8A%B1')
    response=requests.get('http://music.taihe.com/search/song?s=1&key=%E5%88%98%E5%BE%B7%E5%8D%8E&jump=0&start=40&size=20&third_type=0')
    response.encoding = response.apparent_encoding
    #print(response.text)
    doc=pq(response.text)
    a=doc('.search-result-container li').items()
    for item in a:
        a1=pq(item)
        if a1.has_class('search-message-gray'):
            #print('1111')
            pass
        else:
            if a1.attr('data-songitem'):
                #dict=a1.attr('data-songitem')
                dict =json.loads(a1.attr('data-songitem'))
                #print(dict['songItem']['sid'])
                songid=dict['songItem']['sid']
                get_music(songid)

    # print(set(songids))
    # for songid in set(songids):
    #     get_music(songid)
if __name__ == '__main__':
    get_onePage_vip_music()