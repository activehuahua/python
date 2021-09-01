
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         addFormula
# Description:  
# Author:       alex
# Date:         2021/9/1
#-------------------------------------------------------------------------------

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 5) # Outputs 5
worksheet.write(0, 1, 2) # Outputs 2
worksheet.write(1, 0, xlwt.Formula('A1*B1')) # Should output "10" (A1[5] * A2[2])
worksheet.write(1, 1, xlwt.Formula('SUM(A1,B1)')) # Should output "7" (A1[5] + A2[2])
workbook.save('Excel_Formula.xls')