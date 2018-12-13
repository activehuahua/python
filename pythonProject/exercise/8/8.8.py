import  string
def factorial(num):
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    return sum

if __name__=='__main__':
    prompt=input('Please input a num:')
    while prompt.lower()!='q' and int(prompt)>0:
      list2=factorial(int(prompt))
      print(list2)
      prompt=input('Please input a num:')