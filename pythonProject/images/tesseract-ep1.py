#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : tesseract-ep1.py
@Time    : 2018/12/8 10:35
@desc   :
'''

import  tesserocr
from PIL import Image

# image= Image.open(r'image.png')
# image_str=tesserocr.image_to_text(image)
#
# image_str=image_str.replace("'",'')
# print(image_str)
def image_code(filename):
    image=Image.open(filename)
    image=image.convert('L')
    threshold=127
    table=[]
    for i in range(256):
        if i<256:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,'1')

    result=tesserocr.image_to_text(image)
    print(result)


for i in range(1,4):
    try:

        imageName=str(i)+'.png'
        image=Image.open(imageName)
        image_str = tesserocr.image_to_text(image)

        image_str = image_str.replace("'", '')
        print(image_str)

    except Exception as e:
        print(e)
    finally:
        pass

