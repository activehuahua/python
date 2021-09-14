def _ord_iter():
    n=1
    while True:
        n=n+2
        yield  n

def _not_divisible(n):
    result= lambda x : x % n > 0
    return result

def primes():
    yield 2
    it=_ord_iter()
    # print(it)
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible,it)
global num
num=0
for n in primes():

    if n<20:
        print(n, end=' ')
        num+=1
        #print('num=',num)
        if num%10==0:
            print('\n')
    else:
        break