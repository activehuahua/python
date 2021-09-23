# -*- coding: utf-8 -*-#

'''
# Name:         getImageByAlbumID
# Description:  
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

            for i in range(len(result)):
                print(result[i])
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
        if(os.path.exists('images')):
            pass
        else:
            os.mkdir('images')

        if(os.path.exists('images'+os.sep+self.__image_dict['artist_name'])):
            pass
        else:
            os.mkdir('images'+os.sep+self.__image_dict['artist_name'])

        for i in range(len(self.__image_dict)):
            url=self.getLarge_image_url(eval(self.__image_dict['image_id']))
            img=requests.get(url,headers=self.header)
            with open('images'+os.sep+self.__image_dict['artist_name']+os.sep+self.__image_dict['artist_name']+'-'+self.__image_dict['image_id']+'-'+self.__image_dict['title']+'.jpg','ab') as f:
                f.write(img.content)

    def writeToTextFile(self,content):
        with open('content.txt','a', encoding='UTF-8') as f:
            f.write(content)


if __name__ == '__main__':
    # url = 'https://stock.tuchong.com/topic?topicId=50064'
    topicList=[49770]
    for i in range(len(topicList)):
        url='https://stock.tuchong.com/topic?goodsType=0&page=2&size=100&topicId='+str(topicList[i])
        # topicId = common.getTopicId(url)

        album = getImageByAlbumID()
        content=album.getHtml(url)
        album.writeToTextFile(content)
        album.getImageID(content)

