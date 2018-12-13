aList=[5,2,5,6,7,9,1,11,20]
aList.sort()
print(aList)
a=[]
for i in range(len(aList)):
    b=str(aList[i])
    a.append(b)
a.sort()
print(a)

print(max(aList))
print(min(aList))