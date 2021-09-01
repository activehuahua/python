
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         FontColor
# Description:  
# Author:       alex
# Date:         2021/9/1
#-------------------------------------------------------------------------------

from xlsxwriter.workbook import Workbook
workbook = Workbook(r'test.xlsx') # 创建xlsx
worksheet = workbook.add_worksheet('A') # 添加sheet
red = workbook.add_format({'color':'red'}) # 颜色对象
worksheet.write(0, 0, 'sentences') # 0，0表示row，column，sentences表示要写入的字符串
test_list = ["我爱", "中国", "天安门"]
test_list.insert(1, red) # 将颜色对象放入需要设置颜色的词语前面
print(test_list)
worksheet.write_rich_string(1, 0, *test_list) # 写入工作簿
workbook.close() # 记得关闭
