# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 18:57
# @Author  : zhaojianghua
# @File    : json-ep3.py
# @Software: PyCharm
# @Desc    :

import json
#dicts='''
 #{"status": 1, "content": [{"domain": ".weibo.cn", "expiry": 1551265613.942784, "httpOnly": true, "name": "M_WEIBOCN_PARAMS", "path": "/", "secure": false, "value": "uicode%3D20000174"}, {"domain": ".weibo.cn", "expiry": 1582801011.208014, "httpOnly": true, "name": "SUB", "path": "/", "secure": false, "value": "_2A25xchyLDeRhGeBP6FYZ8ifNzT-IHXVSnKTDrDV6PUJbkdANLVf2kW1NRV9EBwAYTYuyMzk3P4MbSySEbbN6_lRE"}, {"domain": ".weibo.cn", "expiry": 1551268613.942589, "httpOnly": false, "name": "MLOGIN", "path": "/", "secure": false, "value": "1"}, {"domain": ".weibo.cn", "expiry": 1866625011.208132, "httpOnly": true, "name": "SCF", "path": "/", "secure": false, "value": "AmnORJ6XLEviWOnoWeht6YQQJgqZ2NGIq7UbBQXTfE-iJUEtj29b5kaN1HaXTPsKwaNl8bSs_aMOWJkYp8Ir2DA."}, {"domain": ".weibo.cn", "expiry": 1582801011.208082, "httpOnly": false, "name": "SUHB", "path": "/", "secure": false, "value": "0k1yj6MRcC58HP"}, {"domain": ".weibo.cn", "httpOnly": false, "name": "SSOLoginState", "path": "/", "secure": false, "value": "1551264987"}, {"domain": ".weibo.cn", "httpOnly": true, "name": "WEIBOCN_FROM", "path": "/", "secure": false, "value": "1110006030"}, {"domain": ".weibo.cn", "expiry": 1553857012.361374, "httpOnly": false, "name": "_T_WM", "path": "/", "secure": false, "value": "e33f3b4a9a836018c970ab27bc16903d"}, {"domain": ".weibo.cn", "httpOnly": false, "name": "XSRF-TOKEN", "path": "/", "secure": false, "value": "153197"}]}
#'''
dicts='''
{"status": 1, "content": [{"domain": ".weibo.cn", "expiry": 1551266772.76486, "httpOnly": true, "name": "M_WEIBOCN_PARAMS", "path": "/", "secure": false, "value": "uicode%3D20000174"}, {"domain": ".weibo.cn", "expiry": 1582802170.457913, "httpOnly": true, "name": "SUB", "path": "/", "secure": false, "value": "_2A25xcgEzDeRhGeBP6FYZ8ifNzT-IHXVSnK97rDV6PUJbkdAKLWLTkW1NRV9EB5JcC0cCgtKnCsY9x7S_oCnYqq5j"}, {"domain": ".weibo.cn", "expiry": 1551269772.764711, "httpOnly": false, "name": "MLOGIN", "path": "/", "secure": false, "value": "1"}, {"domain": ".weibo.cn", "expiry": 1866626170.458084, "httpOnly": true, "name": "SCF", "path": "/", "secure": false, "value": "AmnORJ6XLEviWOnoWeht6YQQJgqZ2NGIq7UbBQXTfE-igN9geZ6HDPIMT-Pbj1ZKGQa0f1fvwvwG9l-9lPwaucA."}, {"domain": ".weibo.cn", "expiry": 1582802170.458013, "httpOnly": false, "name": "SUHB", "path": "/", "secure": false, "value": "0ftZVfRnjGDXMz"}, {"domain": ".weibo.cn", "httpOnly": false, "name": "SSOLoginState", "path": "/", "secure": false, "value": "1551266147"}, {"domain": ".weibo.cn", "httpOnly": true, "name": "WEIBOCN_FROM", "path": "/", "secure": false, "value": "1110006030"}, {"domain": ".weibo.cn", "expiry": 1553858171.40881, "httpOnly": false, "name": "_T_WM", "path": "/", "secure": false, "value": "d9c1085d6820da1f168757e4e574cd1a"}, {"domain": ".weibo.cn", "httpOnly": false, "name": "XSRF-TOKEN", "path": "/", "secure": false, "value": "22afb3"}]}
'''

dicts=dicts.replace("'","\"").replace("True","true").replace("False","false")
json_str=json.loads(dicts)
#print(json_str.get('content'))

for item in range(len(json_str.get('content'))):
    print(json_str.get('content')[item])