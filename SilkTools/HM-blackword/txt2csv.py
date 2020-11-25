#!/usr/bin/python3
# -*-coding:utf-8 -*-
# -*-coding:utf-8 -*-
import csv

with open('file.csv', 'w+', newline='', encoding='UTF-8') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    # 读要转换的txt文件，文件每行各词间以@@@字符分隔
    with open('1.txt', 'r', encoding='UTF-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split(';')
            spamwriter.writerow(line_list)