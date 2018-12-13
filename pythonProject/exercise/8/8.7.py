import  string
def getfactors(num):
    list1=[1]
    count=num//2
    while count>1:
        if num % count==0:
            list1.append(count)
        count-=1
    wanqushu(list1,num)

def wanqushu(list1,num):
    sum=0
    for i in range(len(list1)):
        sum=sum+list1[i]
    if sum==num:
       print(list1,num)

if __name__=='__main__':
    # prompt=input('Please input a num:')
    # while prompt.lower()!='q':
    #   getfactors(int(prompt))
    #   prompt=input('Please input a num:')
    for i in range(1001):
        getfactors(i)