
# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         colorSet
# Description:  
# Author:       alex
# Date:         2021/9/1
#-------------------------------------------------------------------------------

import xlwt

def setStyel(fontName,styleName):
    style=xlwt.XFStyle()
    font=xlwt.Font()
    font.name=fontName
    font.colour_index=3
    style.font=font
    return style

if __name__ == '__main__':

    f=xlwt.Workbook()
    sheet1=f.add_sheet('a')

    sheet1.write(0,0,'My Text',setStyel('Arial','red'))
    f.save('colorSet.xls')

