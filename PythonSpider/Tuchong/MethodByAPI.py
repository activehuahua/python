
# -*- coding: utf-8 -*-#

'''
# Name:         MethodByAPI
# Description:  通过接口接口下载对应的图片
# Author:       alex
# Date:         2021/9/30
# URL:         https://stock.tuchong.com/api/topic?goods_type=0&page=1&size=200&topic_id=50064
'''

from common import *
import requests, re, json, faker
from faker import Faker
import os,sys,string
import math


class getImageByAlbumID():
    def __init__(self):
        self.__image_dict={}
        self.topicId=0
        self.totalNum=0
        self.topic=''

    def setTopic(self,topicId):
        self.topicId=topicId

    def setTopicTitle(self,topic):
        self.topic=topic

    def setTotalNum(self,total):
        self.totalNum=total

    def setHeader(self):
        ua = Faker()
        self.header = {}
        self.header['user-agent'] = ua.user_agent()

    def getHtml(self, url):
        self.setHeader()
        req = requests.get(url, headers=self.header)
        return req

    def getResponse(self,url):
        self.setHeader()
        response = requests.get(url, headers=self.header)
        json_response = json.loads(response.content)
        return json_response

    def getResponse(self,pageNum=1):
        self.setHeader()
        url='https://stock.tuchong.com/api/topic?goods_type=0&page='+str(pageNum)+'&size='+str(self.totalNum)+'&topic_id='+str(self.topicId)
        response = requests.get(url, headers=self.header)
        json_response = json.loads(response.content)
        total=int(json_response['data']['total'])
        # total=math.ceil(total/100.0)
        self.setTotalNum(total)

        topic=str(json_response['data']['topic']['title']).replace('/','').replace('\n','').replace('\r','')

        self.setTopicTitle(topic)
        return json_response

    def getTotalNum(self,response):
        json_response=json.loads(response.content)
        total=int(json_response['data']['total'])
        total=math.ceil(total/100.0)
        self.setTotalNum(total)

    def getImages(self):
        # for i in range(self.totalNum):
            response=self.getResponse(1)
            itemsNums=len(response['data']['goods_list'])

            for item in range(0,itemsNums):
                try:
                    self.__image_dict['image_id']=response['data']['goods_list'][item]['image_id']
                    self.__image_dict['artist_name']=response['data']['goods_list'][item]['artist_name']
                    self.__image_dict['title']=str(response['data']['goods_list'][item]['title']).replace('\n','').replace('\r','')
                    self.downloadImages(item)
                except:
                    continue


    def getLarge_image_url(self,image_id):
        url=f'https://cdn6-banquan.ituchong.com/weili/l/{image_id}.webp'
        return url

    def downloadImages(self,item):
        if not os.path.exists('images'):
            os.mkdir('images')

        if not os.path.exists('images'+os.sep+self.topic):
            os.mkdir('images'+os.sep+self.topic)

        url=self.getLarge_image_url(eval(self.__image_dict['image_id']))
        img=requests.get(url,headers=self.header)

        filename='images'+os.sep+self.topic+os.sep+self.__image_dict['artist_name']+'-'+str(item)+'-'+self.__image_dict['title']+'.jpg'

        if not os.path.exists(filename):
            with open(filename,'ab') as f:
                     f.write(img.content)
                     print('Downloading the file ',filename)

    def writeToTextFile(self,response):

        with open('content.txt','w+') as f:
           f.write(json.dumps(response))


if __name__ == '__main__':
     # topicList=[50064,49770] 49202
     topicList = [50064]
     for i in range(0,len(topicList)):
            url='https://stock.tuchong.com/api/topic?goods_type=0&page=1&size=100&topic_id='+str(topicList[i])

            album = getImageByAlbumID()
            album.setTopic(topicList[i])

            response=album.getResponse(1)
            album.writeToTextFile(response)
            album.getImages()

