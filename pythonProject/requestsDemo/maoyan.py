import requests, re
import json
import time
from requests.exceptions import RequestException
url = 'https://maoyan.com/board/4'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}


def get_html(pageUrl):
    try:
        req = requests.get(pageUrl, headers=headers)
        # print(req.text)
        if(req.status_code == 200):
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

    # for item in result:
    #     print(item[0],item[1],item[2],item[3],item[4],item[5])
    for item in result:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+ item[6]
        }
    return result

def write_to_file(content):
    with open('maoyan.txt','a',encoding='UTF-8') as f:
        #f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.write(str(content)+'\n')

def get_all_urls():
    url_list = []
    for item in range(0, 100, 10):
        url_list.append(url + '?offset=' + str(item))
   # print(url_list)
    return url_list


# parse_movie_info(get_html(url))

# get_all_urls()
if __name__ == '__main__':
    urls = get_all_urls()
    totalPages = len(urls)
    for item in range(totalPages):
        print(urls[item])
        #write_to_file(parse_movie_info(get_html(urls[item])))
        html=get_html(urls[item])
        for content in parse_movie_info(html):
            print(content)
            write_to_file(content)
