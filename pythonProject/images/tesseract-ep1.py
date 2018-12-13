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

image= Image.open(r'image.png')

for i in range(2):
    try:
        j=i+1
        imageName=str(j)+'.jpg'
        image=Image.open(imageName)
        print(tesserocr.image_to_text(image))
    except Exception as e:
        print(e)
    finally:
        pass

