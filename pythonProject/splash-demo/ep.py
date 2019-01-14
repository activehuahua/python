# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 16:54
# @Author  : zhaojianghua
# @File    : ep.py
# @Software: PyCharm
# @Desc    : render.html 输出渲染后的网页，不用splash，获取的就不是渲染后的页面
# render.png 获取截图

import requests
from urllib.parse import quote
from pprint import pprint
import json
#render.html
url='http://192.168.99.100:8050/render.html?url=https://www.baidu.com'
#url='https://www.baidu.com'
# response=requests.get(url)
# print(response.text)

#render.png
url2='http://192.168.99.100:8050/render.png?url=https://www.baidu.com&wait=5&width=1000&height=700'
# response=requests.get(url2)
# with open('taobao.png','wb') as f:
#     f.write(response.content)

#render.json
url3='http://192.168.99.100:8050/render.json?url=https://httpbin.org'
# response=requests.get(url3)
# print(response.text)

#execute
lua='''
function main(splash, args)
  local treat=require("treat")     
  local response=splash:http_get("http://httpbin.org/get")
  return {
    html=treat.as_string(response.body),
    url=response.url,
    status=response.status
    
  }
end
'''

url4='http://192.168.99.100:8050/execute?lua_source='+quote(lua)
response=requests.get(url4)
#response=json.loads(response.text,encoding='utf-8')
print(response.text)