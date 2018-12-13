#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"

from urllib import request


url='http://wap.fc.igemi.cn/pwap/zdyllb'
req = request.Request(url=url)

header = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 MicroMessenger/6.1.4 NetType/3G+'
req.add_header('User-Agent',header)


with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read())