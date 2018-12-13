
# -*- coding: utf-8 -*-
'''
@Author  : zhaojianghua
@File    : string_dict.py
@Time    : 2018/11/22 18:11
'''

dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
#print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))

print ("Sex 值为 : %s" %  dict['Name'])

print ("Value : %s" %  dict.items())

print ("Value : %s" %  str(dict))

dict = {200:'a',20:'b',610:'c'}
d1={}
for k in sorted(dict.keys()) :
    d={k:dict[k]}
    d1.update(d)
print(d1.)