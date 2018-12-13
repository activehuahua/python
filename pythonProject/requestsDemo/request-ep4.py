#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : request-ep4.py
@Time    : 2018/12/12 18:09
@desc   :
'''

import requests, re,string
import urllib.request

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
url = 'http://daily.zhihu.com'


def get_html(url):
    r = requests.get(url, headers=header)
    html = r.text
    return html
    # html = urllib.request.urlopen(url).read()
    # html = html.decode('utf-8')
    # return html


def get_URLs(html):
    pattern = re.compile('<a href="(/story/[\d]+)')
    urls = []
    storys = re.findall(pattern, html)
    for item in storys:
        urls.append(url + item)
    return urls


def get_content(story_url):
    html = get_html(story_url)
    print(story_url)
    pattern = re.compile('<title>(.*?)</title>')
    title = re.findall(pattern, html)
    print(str(title))

    pattern = re.compile('div class="content">\\n<p>(.*?)</div>', re.S)
    content = re.findall(pattern, html)
    for item in content:
        item = item.replace('<p>', '')
        item = item.replace('</p>', '')
        item = item.replace('<strong>', '')
        print(item)


# print(content)

for item in get_URLs(get_html(url)):
    get_content(item)

# html=get_html(url)
# urls=get_URLs(html)
