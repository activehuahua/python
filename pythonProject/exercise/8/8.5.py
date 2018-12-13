import  string
def getfactors(num):
    list1=[num,1]
    count=num//2
    while count>1:
        if num % count==0:
            list1.append(count)
        count-=1
    return  list1

if __name__=='__main__':
    prompt=input('Please input a num:')
    while prompt.lower()!='q':
      list2=getfactors(int(prompt))
      list2.sort()
      print(list2)
      prompt=input('Please input a num:')