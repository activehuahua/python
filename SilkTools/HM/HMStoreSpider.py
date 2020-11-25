import json
import requests
from requests.exceptions import RequestException
import re
import xlwt

from pyquery import PyQuery as pq
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    doc = pq(html)
    a = doc('.toggle-list-item').items()


    for item in a:
        a1=pq(item)
        cityName = a1('h3').text()

        storelist=a1('.stores-list').items()

        for item in storelist:
            store=pq(item)
            p=store('p').text()

            p1=p.split(' ')[-1]

            yield {
            'city':cityName,
            'name':store('h4').text(),
            'address':store('address').text(),
            'time':store('p time').text(),
            'tel':p1
                  }

def excel(items):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sheet1')

        titles = [
            'locale',
            'code',
            'name',
            'phone',
            'service_time',
            'address',
            'region',
            'city',
            'longitude',
            'latitude',
            'status'
        ]
        for title in titles:
            worksheet.write(0, titles.index(title), label=title)
        for item in items:
            num = items.index(item) + 1  # 行
            worksheet.write(num, 0, f'"en_cn"')
            worksheet.write(num, 1, '"CN000"'+ f'"{str(num)}"')
            worksheet.write(num, 2,  f'''"{item['name']}"''')
            worksheet.write(num, 3, f'''"{item['tel']}"''')
            worksheet.write(num, 4,  f'''"{item['time']}"''')
            worksheet.write(num, 5,  f'''"{item['address']}"''')
            worksheet.write(num, 6, f'''"{item['city']}"''')
            worksheet.write(num, 7, f'''"{item['city']}"''')
            worksheet.write(num, 8, f'"121.526254113159"')
            worksheet.write(num, 9, f'"29.8960582339781"')
            worksheet.write(num, 10, f'"1"')
        workbook.save('./parse_en.xls')

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def getStoreInfo():
    url = 'https://www.hm.com.cn/en_cn/customer-service/shopping-at-hm/store-locator-list'
    html = get_one_page(url)

    storelist=list(parse_one_page(html))
    print(len(storelist))
    # print(type(storelist))
    # print(storelist)
    # for item in parse_one_page(html):
    #     print(item)
    excel(storelist)
        # write_to_file(item)


if __name__ == '__main__':
    getStoreInfo()

