import string
def num_changeTo_time(num):
    num=int(num)
    print('%d hours and and %d  minutes  '%(num//60,num%60))

if __name__=='__main__':
    num=input('Please input a number: ');
    while True:
        if not num.isdigit():
            print('Input is invalid, please input again:')
            num=input('Please input a number: ');
        else:
            num_changeTo_time(num)
        num=input('Please input a number: ');

