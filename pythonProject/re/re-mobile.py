# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 17:50
# @Author  : zhaojianghua
# @File    : re-mobile.py
# @Software: PyCharm
# @Desc    :

import re
import  pandas as pd
from pandas import DataFrame
import xlwt,xlrd,xlsxwriter

def getContent():
    result=[]
    with open('CallLogTable.txt','r+') as f:
        result= f.readlines()
    #print(result)

    return result

def getNumber(result):
    content=''.join(result)
    pattern=re.compile('NUMBER:([\d]+)\n')
    numbers = re.findall(pattern, content)
    print(numbers)
    return numbers

def save_to_excel(filename):
    #book=xlrd.open_workbook('numbers.xlsx')
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet('通话记录')
    first_col=sheet.col(0)
    first_col.width=256*50

    book.save(filename)

    result = getContent()
    numbers = getNumber(result)
    df = DataFrame(numbers,columns=['电话号码'])
    df.to_excel(filename, sheet_name='通话记录1', index=False)

    # book=xlrd.open_workbook(filename)
    # sheet=book.sheet_by_index(0)
    # first_col=sheet.col(0)
    # first_col.width = 256 * 50
    book=xlsxwriter.Workbook()


if __name__ == '__main__':
    save_to_excel('numbers.xlsx')
