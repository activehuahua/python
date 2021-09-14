
# -*- coding: utf-8 -*-#

'''
# Name:         dirops
# Description:  
# Author:       alex
# Date:         2021/9/9
'''
import os

# print ('***获取当前目录***')
# print (os.getcwd())
# print (os.path.abspath(os.path.dirname(__file__)))
#
# print ('***获取上级目录***')
# print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print (os.path.abspath(os.path.dirname(os.getcwd())))
# print (os.path.abspath(os.path.join(os.getcwd(), "..")))
#
# print ('***获取上上级目录***')
# print (os.path.abspath(os.path.join(os.getcwd(), "../..")))

current_path=os.getcwd()
parent_path=os.path.dirname(current_path)
grand_path=os.path.dirname(parent_path)

print(current_path)
print(parent_path)
print(grand_path)