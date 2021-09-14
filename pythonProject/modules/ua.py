
# -*- coding: utf-8 -*-#

'''
# Name:         ua
# Description:  
# Author:       alex
# Date:         2021/9/14
'''

from fake_useragent import UserAgent
from faker import Faker

# ua = UserAgent()
# print(ua.random)

ua=Faker()
print(ua.user_agent())