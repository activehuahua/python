aList=[91,92,93,94,95,96,96,98]

sum=0.

for i in range(len(aList)):
    sum+=aList[i]

avg=sum/len(aList)
print('%.2f'%avg)
