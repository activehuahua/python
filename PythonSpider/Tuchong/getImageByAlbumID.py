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


class getImageByAlbumID():
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
        goods='''
        goods=[{"image_id":"237618249672425474","image_source":"tuchong_genius","artist_id":"tuchong_genius~gF0Y65WViSNw62QfYc0tC~OBMO2eqg","artist_name":"沉默的剑心","usage":1,"copyright_type":0,"has_model_release":false,"has_property_release":false,"is_exclusive":false,"is_royalty_free":true,"width":5339,"height":3003,"file_size":5699330,"format":"jpeg","title":"日晷","remark":"","keywords":["建筑","震撼","独特","上海","造型","闪耀","现代","金属感","移动","光","日晷","相对","古老","钟","时刻","计时","道路","古今","复古建筑","概念","设计","无人"],"language":"","title_original":"","remark_original":"","keywords_original":[],"special_remark":"","uploaded_at":1503471337,"enable_platforms":[],"bought":false,"collected":false},{"image_id":"952977660211101708","image_source":"tuchong_genius","artist_id":"tuchong_genius~gF0Y65WViSNw62QfYc0tC~OBMO2eqg","artist_name":"沉默的剑心","usage":1,"copyright_type":0,"has_model_release":false,"has_property_release":false,"is_exclusive":false,"is_royalty_free":true,"width":7952,"height":5304,"file_size":24564607,"format":"jpeg","title":"赛里木湖日出 日照金山","remark":" ","keywords":["雪","山","冰","冰川","景观","没有人","雪山","赛里木湖","风景","风光","旅行","黎明","金山","湖泊","结冰","冬季","寒冷","冷暖","阳光","山峰"],"language":"","title_original":"","remark_original":"","keywords_original":[],"special_remark":"","uploaded_at":1546339992,"enable_platforms":[],"bought":false,"collected":false},{"image_id":"1101486376488140821","image_source":"tuchong_genius","artist_id":"tuchong_genius~gF0Y65WViSNw62QfYc0tC~OBMO2eqg","artist_name":"沉默的剑心","usage":1,"copyright_type":0,"has_model_release":false,"has_property_release":false,"is_exclusive":false,"is_royalty_free":true,"width":7952,"height":5304,"file_size":16296910,"format":"jpeg","title":"一年四季都风景如画的清西郊野公园","remark":" ","keywords":["森林","公园","郊野公园","清西郊野公园","上海","树","红衫","清晨","环境优美","画","树林","绿色","原生态","自然","美景","风景","水杉","水上森林","初冬","逆光","日出","光影"],"language":"","title_original":"","remark_original":"","keywords_original":[],"special_remark":"","uploaded_at":1542957883,"enable_platforms":[],"bought":false,"collected":false}];'''
        # pattern=re.compile('goods=(.*)\n</script>',re.S)
        goods=goods.replace(';','')
        print(goods)
        # pattern=re.compile('goods=(.*)\n.*',re.S)
        pattern = re.compile('goods=(.*)', re.S)
        result=re.findall(pattern,goods)


        print(type(result))
        for i in range(len(result)):
            print(result[i])

    def downloadImages(self):
        pass

    def logImages(self):
        pass

    def writeToTextFile(self,content):
        with open('content.txt','a', encoding='UTF-8') as f:
            f.write(content)


if __name__ == '__main__':
    url = 'https://stock.tuchong.com/topic?topicId=50064'
    topicId = common.getTopicId(url)

    print(topicId)

    album = getImageByAlbumID()
    content=album.getHtml(url)
    album.writeToTextFile(content)
    album.getImageID(content)
