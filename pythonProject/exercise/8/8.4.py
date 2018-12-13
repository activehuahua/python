import  string
def isPrime(num):
    count=num//2
    isPrimeNum=True
    while count>1:
        if num % count==0:
            isPrimeNum=False
        count-=1
    return  isPrimeNum

if __name__=='__main__':
    # prompt=input('Please input a num:')
    # while prompt.lower()!='q':
    #   print(isPrime(int(prompt)))
    #   prompt=input('Please input a num:')
    list1=[]
    for i in range(1,101):
        if isPrime(i):
            list1.append(i)
    print(list1)