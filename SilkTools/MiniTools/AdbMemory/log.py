# coding = utf-8

import re
import xlwt



class Log():
    def __init__(self):
        self.file = open('./meminfo_detail.txt', 'r', encoding='utf-8').read()


    def parse(self):
        split_str = 'App Summary'
        split_file = self.file.split(split_str)

        Java_Heap_re = 'Java Heap:     (.*?)                          (.*?)\n'
        Native_Heap_re = 'Native Heap:    (.*?)                          (.*?)\n'
        Code_re = 'Code:    (.*?)                         (.*?)\n'
        Stack_re = 'Stack:     (.*?)                           (.*?)\n'
        Graphics_re = 'Graphics:    (.*?)                          (.*?)\n'
        Private_Other_re = 'Private Other:     (.*?)\n'
        System_re = 'System:    (.*?)\n'
        TOTAL_PSS_re1 = 'TOTAL PSS:   (.*?) '
        TOTAL_PSS_re2 = 'TOTAL PSS:   (.*?)  '
        TOTAL_RSS_re = 'TOTAL RSS:   (.*?)  '
        TOTAL_SWAP_PSS_re = 'TOTAL SWAP PSS:       (.*?)\n'

        all_item = []
        for i in split_file[1:]:
            every_item = []
            Java_Heap = re.findall(Java_Heap_re, i)
            Native_Heap = re.findall(Native_Heap_re, i)
            Code = re.findall(Code_re, i)
            Stack = re.findall(Stack_re, i)
            Graphics = re.findall(Graphics_re, i)
            Private_Other = re.findall(Private_Other_re, i)
            System = re.findall(System_re, i)
            TOTAL_PSS = re.findall(TOTAL_PSS_re1, i)
            if TOTAL_PSS == ['']:
                TOTAL_PSS = re.findall(TOTAL_PSS_re2, i)
            TOTAL_RSS = re.findall(TOTAL_RSS_re, i)
            TOTAL_SWAP_PSS = re.findall(TOTAL_SWAP_PSS_re, i)

            every_item.append(Java_Heap[0])
            every_item.append(Native_Heap[0])
            every_item.append(Code[0])
            every_item.append(Stack[0])
            every_item.append(Graphics[0])
            every_item.append(Private_Other[0])
            every_item.append(System[0])
            every_item.append(TOTAL_PSS[0].strip())
            every_item.append(TOTAL_RSS[0])
            every_item.append(TOTAL_SWAP_PSS[0])
            all_item.append(every_item)
        return all_item


    def excel(self, items:list):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('sheet1')

        titles = [
            '序号',
            'Java Heap Pss(KB)',
            'Java Heap Rss(KB)',
            'Native Heap Pss(KB)',
            'Native Heap Rss(KB)',
            'Code Pss(KB)',
            'Code Rss(KB)',
            'Stack Pss(KB)',
            'Stack Rss(KB)',
            'Graphics Pss(KB)',
            'Graphics Rss(KB)',
            'Private Other Pss(KB)',
            'System Pss(KB)',
            'TOTAL PSS(KB)',
            'TOTAL RSS(KB)',
            'TOTAL SWAP PSS',
        ]
        for title in titles:
            worksheet.write(0, titles.index(title), label=title)
        for item in items:
            num = items.index(item) + 1    # 行
            worksheet.write(num, 0, label=num)
            for element in item:
                element_num = item.index(element) + 1    # 列
                if element_num < 6:
                    pss, rss = element[0], element[1]
                    worksheet.write(num, element_num*2-1, label=pss)
                    worksheet.write(num, element_num*2, label=rss)
                else:
                    worksheet.write(num, element_num+5, label=element)

        workbook.save('./parse.xls')


    def main(self):
        all_items = self.parse()
        self.excel(all_items)



if __name__ == '__main__':
    Log().main()