# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 17:19
# @Author  : zhaojianghua
# @File    : getPhoneNum.py
# @Software: PyCharm
# @Desc    :

import re
import  pandas as pd
from pandas import DataFrame

def getContent():
    result=[]
    with open('CallLogTable.txt','r+') as f:
        for line in f.readlines():
            # pattern =re.compile('NUMBER:[\d]+(\.?)')
            # number = re.search(pattern, line)
            # if number:
            #     result.append(number)
    #result=result.replace("\n","")
             if 'NUMBER:' in line:
                 line=line.replace("NUMBER:",'').replace("\n",'')
                 result.append(line)
    print(result)

    return result



if __name__ == '__main__':
    result=getContent()
    df=DataFrame(result)
    df.to_excel('number.xlsx')
