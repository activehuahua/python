import requests, re
import json
import time
from requests.exceptions import RequestException
from PIL import Image
import os, string

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}


def get_html(pageUrl):
    try:
        req = requests.get(pageUrl, headers=headers)
        # print(req.text)
        if (req.status_code == 200):
            html = req.text
            return html
        return None
    except RequestException as e:
        return None


def parse_movie_info(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        re.S)
    result = re.findall(pattern, html)

    for item in result:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    return result


def write_to_file(content):
    with open('maoyan.txt', 'a', encoding='UTF-8') as f:
        # f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.write(str(content) + '\n')


def get_all_urls():
    url_list = []
    for item in range(0, 100, 10):
        url_list.append(url + '?offset=' + str(item))
    return url_list

def save_pic_local(content):
    if (os.path.exists('imgs')):
        pass
    else:
        os.mkdir('imgs')
    img = content['image']
    img_real_url = str(img).split('@')[0]
    img = requests.get(img_real_url)
    with open('imgs/' + content['name'] + '.jpg', 'ab') as f:
        f.write(img.content)


if __name__ == '__main__':
    url = 'https://maoyan.com/board/4'
    urls = get_all_urls()
    totalPages = len(urls)
    for item in range(totalPages):
        #   print(urls[item])
        html = get_html(urls[item])
        for content in parse_movie_info(html):
            #  print(content)
            write_to_file(content)
            save_pic_local(content)
