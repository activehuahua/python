#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     day3
   Description :
   Author :       zhaojianghua
   date：          2019/1/6
'''
from imtools import histeq
from PIL import  Image
from numpy import *

im=array(Image.open('1.png').convert('L'))

im2,cdf=histeq(im)

print(im2)
print(cdf )