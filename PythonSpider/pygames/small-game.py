# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 15:14
# @Author  : zhaojianghua
# @File    : small-game.py
# @Software: PyCharm
# @Desc    :

import pygame
import sys

pygame.init()

size = width, height = 800, 400

speed = [1, 1]

bg = (255, 255, 255)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的第一个游戏")

turtle = pygame.image.load("timg.png")

position = turtle.get_rect()  # 获取图形的位置

a = open ("log.txt","w")
while True:
    for event in pygame.event.get():
        a.write(str(event))
        if event.type == pygame.QUIT:
            sys.exit()
        position = position.move(speed)  # 移动图片

    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)  # 翻转图像
        speed[0]=-speed[0]  #反向移动

    if position.top <0 or position.bottom >height:
        speed[1] = -speed[1]

    screen.fill(bg) # 填充背景
    screen.blit(turtle,position) #更新图片
    pygame.display.flip() # 更新界面
    #pygame.time.delay(2) #延迟8秒