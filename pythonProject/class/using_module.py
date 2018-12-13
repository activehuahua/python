'test a module'
__author__='zhaojianghua'

import  sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello, World!')
    elif len(args)==2:
        print('Hello, %s'%(args[1]))
    else:
        print('Too many args')

if __name__=='__main__':
    test()