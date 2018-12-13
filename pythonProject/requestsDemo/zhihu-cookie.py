#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : zhihu-cookie.py
@Time    : 2018/12/13 18:04
@desc   :
'''
import requests

headers={
'cookie': '_zap=ac2810e3-f14c-4e5d-bb69-d932caac5f81; d_c0="AADi7CSWnA6PTgStcV6mJnyAV5mIz7oPm-g=|1543806510"; q_c1=3d166514135b45329a263520c82a5676|1543806512000|1543806512000; l_cap_id="N2NhM2M4NTFlNTJmNDBkYzk1YjZmZGQ0MjBjMGYxZjc=|1544606179|4d007573e3fa527f2e296e68a2fc7781ba5a497b"; r_cap_id="YzgwNTQ2ZDRjZGQ3NDhkYzljNmEyOTgyZWNkMDNkZjk=|1544606179|c37c54eedd90eda7efd9c73613ec61326fc061ca"; cap_id="MWQ3YzFlYTM2ZWFlNDJhZDlmYTE5OTc3YmUwZjFkZmY=|1544606179|21228b1b8c8ab1322187b32ea75c4974215f2d98"; __utma=155987696.268620639.1544608729.1544608729.1544608729.1; __utmz=155987696.1544608729.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.268620639.1544608729; _gid=GA1.2.1902399424.1544609976; tgw_l7_route=27a99ac9a31c20b25b182fd9e44378b8; _xsrf=iH9ef9VpQ4sjEWwcrGJwxvPuKbWJpIf0; capsion_ticket="2|1:0|10:1544695166|14:capsion_ticket|44:Y2IxYmJjZTI1MTc5NGVjZjkwYzQwOWRkY2ZjNjQ4ODc=|a30ecf4b67ecc34d1693597278a5f040229b51c490ef35b0fec0003e82cf6a90"; z_c0="2|1:0|10:1544695211|4:z_c0|92:Mi4xLUZ5TERRQUFBQUFBQU9Mc0pKYWNEaVlBQUFCZ0FsVk5xbnZfWEFEZVNNd3JmdmQ0c1l5R3lmZHNJUHk5REE5b2NR|a20012a8fe4de5ac5cedcc84cf5ae17f1961957bd06c938c1cdeeb414e54f6cf"; tst=r',
'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
}

r = requests.get("https://www.zhihu.com",headers=headers)
print(r.text)