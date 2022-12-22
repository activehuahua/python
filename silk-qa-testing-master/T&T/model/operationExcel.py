from model.pubilc import data_dir,phonenumber
import xlrd
'''
def readExcels(rowValue,colValue):
    book=xlrd.open_workbook(data_dir(fileName="casnhu.xlsx"))
    sheet=book.sheet_by_index(0)
    return sheet.cell_value(rowValue, colValue)
'''
'''
class ReadExcel():
    def readExcels(fileName,SheetName):
        rows=[]
        book=xlrd.open_workbook(data_dir(fileName))
        sheet=book.sheet_by_name(SheetName)

        # 获取总行数
        nrows = sheet.nrows
        cols = sheet.ncols
        if nrows>1:
            # 拿第一行的内容
            keys = sheet.row_values(0)

            for row in range(1,nrows):
                rows.append(dict(zip(keys,sheet.row_values(row))))
            return rows
        else:
            print("表格未填写数据")
        return None
'''
class ReadExcel():
    def readExcels(fileName,SheetName):
        book=xlrd.open_workbook(data_dir(fileName))
        sheet=book.sheet_by_name(SheetName)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        for i in range(rows):
            row_content = []
            for j in range(cols):
                ctype = sheet.cell(i, j).ctype
                cell = sheet.cell_value(i, j)
                if ctype == 2 and cell % 1 == 0:
                    cell = int(cell)
                row_content.append(cell)
            all_content.append(row_content)
        newlist=[]
        if len(all_content)>1:
            key=all_content[0]
            for i in range(1,len(all_content)):
                newlist.append(dict(zip(key,all_content[i])))
        return newlist
if __name__ == '__main__':
     s=ReadExcel.readExcels("login.xlsx","Sheet1")
     print(type(s[0]['expect_txt1']))
     print(type(phonenumber()))


