# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 13:56
# @Author  : zhaojianghua
# @File    : geetest-demo1.py
# @Software: PyCharm
# @Desc    :


'''
滑块验证码
哔哩哔哩 登录验证
'''
from selenium.webdriver.common.action_chains import *
from selenium import webdriver
import time
import random
from PIL import Image

patn = 'chromedriver.exe'
browser = webdriver.Chrome(patn)


# 获取偏移量
def get_distance(image1, image2):
    '''
    拿到滑动验证码需要移动的距离
    :param image1:没有缺口的图片对象
    :param image2:带缺口的图片对象
    :return:需要移动的距离
    '''
    threshold = 60
    left = 57
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threshold and res2 < threshold and res3 < threshold):
                return i - 7  # 经过测试，误差为大概为7

    return i - 7  # 经过测试，误差为大概为7


# 拿到移动轨迹
def get_tracks(distance):
    '''
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ①v=v0+at
    ②s=v0t+½at²
    ③v²-v0²=2as
    :param distance: 需要移动的距离
    :return: 存放每0.3秒移动的距离
    '''
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 0.3
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达mid值开始减速
    mid = distance * 4 / 5

    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = 2
        else:
            a = -3

        # 初速度
        v0 = v
        # 0.2秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t
    return tracks


# 鼠标模拟滑动,按照轨迹拖动，完全验证
def move_slider(tracks):
    ActionChains(browser).click_and_hold(slider).perform()
    for track in tracks:
        ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()
    else:
        ActionChains(browser).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移过一点
        ActionChains(browser).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，是不是更像人了

    time.sleep(0.5)  # 0.5秒后释放鼠标
    ActionChains(browser).release().perform()


if __name__ == '__main__':

    try:
        browser.get('https://passport.bilibili.com/login')
        browser.save_screenshot('lodin.png')

        username = browser.find_element_by_id('login-username')
        password = browser.find_element_by_id('login-passwd')
        # 获取滑块
        slider = browser.find_element_by_xpath('//div[@id="gc-box"]/div/div[3]/div[2]')

        print(slider)
        username.send_keys('账号')
        password.send_keys('密码')

        # 鼠标悬停事件(显示完整图片)
        ActionChains(browser).move_to_element(slider).perform()
        time.sleep(1)
        screenshot = browser.save_screenshot('tu1.png')

        print(type(screenshot))

        time.sleep(2)

        # 鼠标点击(显示残缺图片)
        slider.click()
        time.sleep(3)
        browser.save_screenshot('tu2.png')

        # 获取 图片的位置大小
        img1 = browser.find_element_by_xpath(xpath='//div[@class="gt_cut_fullbg gt_show"]')
        location = img1.location
        size = img1.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        print('图片的宽:', img1.size['width'])
        print(top, bottom, left, right)

        #  保存 裁剪 图片
        img_1 = Image.open('tu1.png')
        img_2 = Image.open('tu2.png')
        capcha1 = img_1.crop((left, top, right, bottom))
        capcha2 = img_2.crop((left, top, right, bottom))
        capcha1.save('tu1-1.png')
        capcha2.save('tu2-2.png')

        # 获取验证码图片
        img_11 = Image.open('tu1-1.png')
        img_22 = Image.open('tu2-2.png')

        distance = get_distance(img_11, img_22)

        tracks = get_tracks(distance)
        print(tracks)
        print(distance, sum(tracks))
        move_slider(tracks)
    except:
        pass

# time.sleep(10)
