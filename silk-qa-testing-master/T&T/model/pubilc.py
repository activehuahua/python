import os
import itertools
import json
import random
def data_dir(fileName,data='data-driven'):
    '''对查找文件路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

# print(data_dir("casnhu.xlsx"))
def phonenumber():
    '''随机生成手机号'''
    phone="150028"
    res=[]
    for i in itertools.permutations(range(1,11),6):
        res.append(i[0]*100000+i[1]*10000+i[2]*1000+i[3]*100+i[4]*10+i[5])
    new=random.sample([phone+str(i) for i in res],1)
    return new[0]

def email():
    '''生成邮箱'''
    email="@sina.com"
    Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    randomNumber = "".join(random.choice(Number) for i in range(1,11))
    Email = randomNumber + email
    return Email

# print(phonenumber())
# x=itertools.permutations(range(1,11),5)
# print(list(x))
# print(email())