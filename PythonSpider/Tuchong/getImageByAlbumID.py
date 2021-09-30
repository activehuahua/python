# -*- coding: utf-8 -*-#

'''
# Name:         getImageByAlbumID
# Description:  通过页面元素解析下载图片
# Author:       alex
# Date:         2021/9/16
#               https://stock.tuchong.com/topic?topicId=50064
'''
from common import *
import requests, re, json, faker
from faker import Faker
import os,sys,string


class getImageByAlbumID():
    def __init__(self):
        self.__image_dict={}

    def setHeader(self):
        ua = Faker()
        self.header = {}
        self.header['user-agent'] = ua.user_agent()

    def getHtml(self, url):
        self.setHeader()
        req = requests.get(url, headers=self.header)
        content = req.text
        # print(content)
        return content

    def getImageID(self,content):

        pattern = re.compile('goods=\[(.*)\];\n</script>', re.S)
        result=re.findall(pattern,content)
        try:
            result=list(eval(result[0].replace('false','False').replace('true','True')))

            for i in range(len(result)-1):
                # print(result[i])
                image_dict={}
                a=result[i]
                newResult=dict(a)
                self.__image_dict['image_id']=newResult['image_id']
                self.__image_dict['artist_name']=newResult['artist_name']
                self.__image_dict['title']=str(newResult['title']).replace('\n','').replace('\r','')
                self.downloadImages()
        except:
            return None

    def getLarge_image_url(self,image_id):
        url=f'https://cdn6-banquan.ituchong.com/weili/l/{image_id}.webp'
        return url

    def downloadImages(self):
        if not os.path.exists('images'):
            os.mkdir('images')

        if not os.path.exists('images'+os.sep+self.__image_dict['artist_name']):
            os.mkdir('images'+os.sep+self.__image_dict['artist_name'])

        url=self.getLarge_image_url(eval(self.__image_dict['image_id']))
        img=requests.get(url,headers=self.header)

        filename='images'+os.sep+self.__image_dict['artist_name']+os.sep+self.__image_dict['artist_name']+'-'+self.__image_dict['title']+self.__image_dict['image_id']+'.jpg'

        if not os.path.exists(filename):
            with open(filename,'ab') as f:
                     f.write(img.content)
                     print('Downloading the file ',filename)

    def writeToTextFile(self,content):
        with open('content.txt','w+', encoding='UTF-8') as f:
            f.write(content)


if __name__ == '__main__':
    # url = 'https://stock.tuchong.com/topic?topicId=50064 ,49770'
    topicList=[50064]
    for i in range(len(topicList)):
        for j in range(10):
            url='https://stock.tuchong.com/topic?goodsType=0&page='+str(j)+'&size=100&topicId='+str(topicList[i])
            # topicId = common.getTopicId(url)

            album = getImageByAlbumID()
            content=album.getHtml(url)
            album.writeToTextFile(content)
            album.getImageID(content)

