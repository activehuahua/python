#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   File Name：     imtools
   Description :
   Author :       zhaojianghua
   date：          2019/1/6
   累积分布函数---》 直方图均衡化的变换函数是图像中的像素值cdf
   归一化--》 将像素值的范围映射到目标范围
'''
from numpy import histogram,interp


def histeq(im, nbr_bins=256):
    # 对一副灰度图像进行直方图的均衡化
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), 256, normed=True)  # 转换为一维图像

    # 累积分布函数使用
    cdf = imhist.cumsum()
    # 归一化操作
    cdf = 255 * cdf / cdf[-1]
    #使用累积分布函数的线性差值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return  im2.reshape (im.shape()),cdf