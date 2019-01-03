#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     weapon
   Description :
   Author :       zhaojianghua
   date：          2019/1/3
   http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json"
                        wl_45": "48",  威力
						"sc_54": "60", 射程
						"ss_d0": "69", 射速
						"wdx_a7": "50", 稳定性
						"zds_62": "40"  子弹数
'''

import requests
import json
import jsonpath  # 抽取枪支信息
import pygal  # 雷达

response = requests.get('http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json')

py_data = json.loads(response.content.decode())
# py_data=json.loads(response.text)

# print(py_data)

name = jsonpath.jsonpath(py_data, "$..mc_94")[1:8]
xinn = jsonpath.jsonpath(py_data, "$..ldtw_f2")

# print(name)
# print(xinn)
data = []
n = 0
for i in xinn:
    if n < 7:
        n += 1
        # print(i)
        data.append(
            [int(i[0]['wl_45']), int(i[0]['sc_54']), int(i[0]['ss_d0']), int(i[0]['wdx_a7']), int(i[0]['zds_62'])])

# print(data,name)
# 调用Radar 设置雷达图
radar_chart = pygal.Radar()
radar_chart.title = "步枪性能"
# 添加雷达图各顶点
radar_chart.x_labels = ["威力", "射程", "射速", "稳定性", "子弹数"]
for  n,d in zip(name,data):
    radar_chart.add(n, d)

# 保存
radar_chart.render_to_file('gun.svg')
