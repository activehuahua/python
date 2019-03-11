# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 13:57
# @Author  : zhaojianghua
# @File    : demo.py
# @Software: PyCharm
# @Desc    :

import requests
from pyquery import PyQuery as pq

url='http://www.ccfdw.gov.cn/ecdomain/lpcs/xmxx/huxx.jsp?hid=40288a8d66a06b190166aebe5db351b0&lid=40288a8d66a06b190166aebe5d94515e'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}
#
# r=requests.get(url,headers=headers)
#
# #print(r.text)
#
# doc=pq(r.text)

# td=doc("tr:first-child td:nth-child(4)")

# td=doc('td').eq(4).text()
# print(td  )
# td=doc('td').eq(28).text()
# print(td  )

result=[]
with open('houselists.txt', 'r') as f:
    singleHouse = f.readlines()
    #singleHouse=str(singleHouse).replace('\\n','')
    result.append(singleHouse)



# print(result)

# for item in result:
#     print(item)
    # list1=item.split(",")
    # print(list1)

list1=result[0]
print(type(list1))
baseurl='http://www.ccfdw.gov.cn/ecdomain/lpcs/xmxx/huxx.jsp'

for item in list1:
    list=item.split(',')
    print(baseurl+'?hid='+list[0]+'&lid='+list[1])

