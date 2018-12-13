import  string

num=6543
str1=str(num)
aList=list(str1)
print(aList)

bList=[]

for i in range(len(str1)):
    bList.append(str1[i]*3)

print('.'.join(bList))

bList.reverse()
print('.'.join(bList))