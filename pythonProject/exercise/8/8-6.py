import  string
def isPrime(num):
    count=num//2
    isPrimeNum=True
    while count>1:
        if num % count==0:
            isPrimeNum=False
        count-=1
    return  isPrimeNum

def getfactors(num):
    list1=[]
    list2=[]
    count=int(num)//2
    while count>1:
        if num % count==0:
            if isPrime(count):
                list1.append(count)
        count-=1

    for i in range(len(list1)):

        num=int(num)//(list1[i])
        list2.append(list1[i])
        while True:
            if num% list1[i]==0:
               list2.append(list1[i])

            else:
                break
            num=int(num)//list1[i]

    return  list2



if __name__=='__main__':
    prompt=input('Please input a num:')
    while prompt.lower()!='q':
      list2=getfactors(int(prompt))
      list2.sort()
      print(list2)
      prompt=input('Please input a num:')