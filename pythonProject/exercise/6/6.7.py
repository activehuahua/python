num_str=input('Enter a number:')
num_num=int(num_str)
aList=[]
fac_list=list(range(1,num_num+1))
print('Before:',fac_list)
print(fac_list)
i=0
length=len(fac_list)
while i<length:
    if num_num % fac_list[i] !=0:
       aList.append(fac_list[i])
    i=i+1

print("After:",aList)