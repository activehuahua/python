#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     day2
   Description :
   Author :       zhaojianghua
   date：          2019/1/6
'''
from PIL import Image
from pylab import  *

#进行灰度处理
im=array(Image.open('1.png').convert('L'))

#新建一个图像
figure()
#不是用颜色

gray()
#在原点的左上角显示轮廓图
contour(im,origin='image')
#画出图像的类型
axis('off')  #灰度图
axis('equal')  #直方图
#新建一个图像
figure()
#hist() --->一维数组， 小区间的数目，
hist(im.flatten(),128)
show()

