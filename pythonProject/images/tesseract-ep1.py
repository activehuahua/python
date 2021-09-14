#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : tesseract-ep1.py
@Time    : 2018/12/8 10:35
@desc   : 使用图片的灰度处理来提高验证码的识别准确率
'''

import tesserocr
from PIL import Image


def deal_table():
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def deal_image(filename):
    image = Image.open(filename)

    # 图片灰度处理
    image = image.convert('L')

    # 将图片进行二值化处理
    image = image.point(deal_table(), '1')
    # image.show()

    result = tesserocr.image_to_text(image)
    print(result)


if __name__ == '__main__':

    for i in range(1, 3):
        try:
            imageName = str(i) + '.png'
            deal_image(imageName)
        except Exception as e:
            print(e)
        finally:
            pass
