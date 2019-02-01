# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 16:20
# @Author  : zhaojianghua
# @File    : sounds.py
# @Software: PyCharm
# @Desc    : 语音合成安装 pip install baidu-aip


from aip import AipSpeech
appid="14975947"
api_key="X9f3qewZCohppMHxlunznUbi"
secret_key = "LupWgIIFzZ9kTVNZSH5G0guNGZIqqTom"

client=AipSpeech(appid,api_key,secret_key)
result=client.synthesis('值此新春佳节之际，祝初唐科技家人们幸福吉祥身体健康，乐驰千里马，更上一层楼!！',"zh",1,{
    "vol":10,  #音量
    "spd":4,   #语速
    "pit":3,   #语调
    "per":3,   #音色
})

file_name='voice.mp3'

if not isinstance(result,dict):
    with open(file_name,'wb') as f:
        f.write(result)