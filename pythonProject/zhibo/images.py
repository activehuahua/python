#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     images
   Description :
   Author :       zhaojianghua
   date：          2019/1/6
'''
from PIL import Image
from pylab import *

im = array(Image.open('1.png'))

imshow(im)

x=[100,100,400,400]
y=[200,500,200,500]

#指定点的颜色和形状
plot(x,y,'r*')

#绘制连接前2点的线
plot(x[:2],y[:2])

#添加title
title('Plotting')

show()