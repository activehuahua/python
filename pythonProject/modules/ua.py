
# -*- coding: utf-8 -*-#

'''
# Name:         ua
# Description:  
# Author:       alex
# Date:         2021/9/14
'''

from faker import Faker

ua=Faker()
for i in range(0,10):
    print(i,ua.user_agent())