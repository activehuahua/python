#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     numbpy
   Description :
   Author :       zhaojianghua
   date：          2019/1/6
   numpy ：python 的科学计算工具包, 图像数组表示
'''

from numpy import *
from PIL import Image

#算法工程师
im=array(Image.open('1.png').convert('L'))
print(im)
print('*******************************')
#简单算法
#对图像进行反相处理
im2=255- im

im3=(100.0/255)*im+100

im4=255.0*(im/255.0)**2
print(im2)
print('*'*50)
print(im3)
print('-'*50)
print(im4)
#像素的最小和最大
print(int(im.min()),int(im.max()))
show()