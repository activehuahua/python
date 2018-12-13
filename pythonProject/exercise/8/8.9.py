def fbnq(num):
    list1=[1,1]
    for i in range(2,num):
        temp=list1[i-2]+list1[i-1]
        list1.append(temp)
    return  list1


if __name__=='__main__':
    prompt=input('Please input a num:')
    while prompt.lower()!='q' and int(prompt)>2:
      list2=fbnq(int(prompt))
      print(list2)
      prompt=input('Please input a num:')