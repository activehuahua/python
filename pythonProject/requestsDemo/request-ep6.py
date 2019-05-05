# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 21:47
# @Author  : zhaojianghua
# @File    : request-ep6.py
# @Software: PyCharm
# @Desc    :

import requests,json,re,string
from time import  sleep


header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    # ,
    # 'Referer':'https://backendappaws.bundleb2b.net/companies',
    # # 'Accept':'application/json, text/plain, */*',
    # 'Host':'backendappaws.bundleb2b.net'
    # ,
    ,'Cookie':'session=c5ff897c-bc3f-487c-a626-1d50bf006e3a'
     #'Cookie':'session=006c71ad-ceae-4e9f-8fd9-fd5bb2973338'#; remember_token=1311854|ce8893ea87e7d4d85cf166fecdd95e9369863168e925a8e6d2fcf333c3ae45d6b983c229e594b36652d8505fdaee12f693e535ed58f6fda6d823fbec64321908'
}


# url='https://fl4mq0bm40.execute-api.us-west-2.amazonaws.com/prod/getListRequistionListNew?store_hash=h3jnjw30qw&company_id=10383960781277499881&customer_id=339'

login_url='https://login.bigcommerce.com/login'
params={
    #'authenticity_token':'3cbwqAd1UbBHCe5rinP0zyOyTFZzRl11xxEhzvbpt9YssBt88XSKXE5swXHw7gkGzWbS+OlYwpWsPOYnGtK2hw==',
    'user[email]':'alexander.zhao@silksoftware.com',
    'user[password]':'Silk@123',
    'commit':'Log in',
    'remember_email':'1'
}
url_app='https://rays-store8.mybigcommerce.com/manage/app/13706'

#url_api='https://backendappaws.bundleb2b.net/'

url_company='https://backendappaws.bundleb2b.net/api/companies'

s=requests.Session()

r=s.post(login_url, headers=header,params=params)
#print(r.text)
sleep(5)
#print(r.cookies)

r1=s.get(url_app,headers=header)

cookies=r1.cookies.get_dict()
print(cookies)

r2=s.get(url_company,headers=header,cookies=cookies)
print(r2.text)

#Json=json.loads(r.content)

#print(len(Json['companylist']))

#print(Json)