
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         mergeCells
# Description:  
# Author:       alex
# Date:         2021/9/1
#-------------------------------------------------------------------------------

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0's columns 0 through 3. 从第0行开始，跨0行；从第0列开始，跨到第3列，总共4列
font = xlwt.Font() # Create Font
font.bold = True # Set font to Bold
style = xlwt.XFStyle() # Create Style
style.font = font # Add Bold Font to Style
worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style) # 从第1行开始，跨到第2行；从第0列开始，跨到3列，总共4列
workbook.save('Excel_Workbook.xls')