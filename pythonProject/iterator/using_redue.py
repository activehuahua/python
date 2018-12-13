from functools import reduce
import  string
import math

def prod(L):
    return  reduce(fn, (map(int ,L)))

def fn(x,y):
    return x*y

def f(x,y):
    return x*10+y

def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
    i=len(s)-s.index('.')-1
    s=s.replace('.','')


    return   reduce(f,map(char2num,s))/math.pow(10,i)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('str2float(\'123.456\') =', str2float('123.456'))