import  string
def myStrip(s):
    aList1=[]
    aList2=[]
    for i in range(len(s)):
        if s[i].isspace():
            continue
        else:
            str2=s[i:]
            break


    for i in range(-1,-len(str2),-1):
        if str2[i].isspace():
            continue
        else:
            if i==-1:
                str3=str2[:]
            else:
                str3=str2[:i+1]
            break
    return  str3


print(myStrip('  1  sssss    1  '))
print(myStrip('  2  sssss    2'))
print(myStrip('  3  ss  sss    3  '))


