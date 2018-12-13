#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : robots-ep1.py
@Time    : 2018/12/12 15:31
@desc   :
'''
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("http://www.jianshu.com/robots.txt")
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/9c3d50ae847d'))
print(rp.can_fetch('trendkite-akashic-crawler', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

print(rp.can_fetch('*', 'http://www.jianshu.com/sign_in'))
