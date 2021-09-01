# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 18:38
# @Author  : zhaojianghua
# @File    : 1.py
# @Software: PyCharm
# @Desc    :

import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet1')
first_col=sheet.col(0)       #xlwt中是行和列都是从0开始计算的
sec_col=sheet.col(1)

first_col.width=256*50

sheet.write(1,2,10)


book.save('width.xls')