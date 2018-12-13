'''
字符串模板
'''

from string import  Template
s=Template('There are ${howmany} ${lang} Quotation Symbols')

print(s.substitute(lang='Python', howmany=3))
