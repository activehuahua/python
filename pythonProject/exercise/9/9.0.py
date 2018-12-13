import os


file=open('test.txt','a+')
file.write('%s%s'%('New line',os.linesep))
file.close()
file=open('test.txt','r')
for eachline in file:
    print(eachline,)

file.close()