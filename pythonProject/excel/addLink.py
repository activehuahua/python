
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         addLink
# Description:  
# Author:       alex
# Date:         2021/9/1
#-------------------------------------------------------------------------------

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, xlwt.Formula('HYPERLINK("http://www.baidu.com";"Baidu")')) # Outputs the text "Google" linking to http://www.google.com
workbook.save('Excel_Workbook1.xls')