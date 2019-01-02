#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     ip
   Description :
   Author :       zhaojianghua
   date：          2019/1/2

   www.ipip.net/ip.html
'''

from tkinter import  *
import requests,re

root=Tk()

root.title("ip地址的查询")




def find_position():
    ip=ip_input.get()
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    html=requests.get('https://www.ipip.net/ip/{}.html'.format(ip),headers=headers).text
    address=re.search(r'地理位置.*?;">(.*?)</span>',html,re.S)
    operator = re.search(r'运营商.*?;">(.*?)</span>', html, re.S)
    time = re.search(r'时区.*?;">(.*?)</span>', html, re.S)
    wrap = re.search(r'地区中心经纬度.*?;">(.*?)</span>', html, re.S)

    #print(address.group(1))
    if address:
        ip_info=['地理位置:'+address.group(1),"当前的IP："+ip]
        if operator:
            ip_info.insert(0,'所有者/运营商:'+operator.group(1))
        if time:
            ip_info.insert(0,'时区:'+time.group(1))
        if wrap:
            ip_info.insert(0,'地区中心经纬度:'+wrap.group(1))
        display_info.delete(0, 5)

        for item in ip_info:
            display_info.insert(0, item)
    else:
        display_info.delete(0, 5)
        display_info.insert(0,"无效的IP")


ip_input=Entry(root,width=40 )

display_info=Listbox(root, width=60,height=10)

result_button=Button(root,command=find_position,text="查询")



if __name__ == '__main__':
    ip_input.pack()
    display_info.pack()
    result_button.pack()

    root.mainloop()