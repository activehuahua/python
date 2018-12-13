import  string

def findchr(string1,char1):
    result=-1
    for i in range(len(string1)):
        if char1==string1[i]:
            result= i
            return  result

    return result

def rfindchar(string1,char1):
    result=-2
    for i in range(-1,-len(string1)-1,-1):
        if char1==string1[i]:
            result=i
            return result
    return result

def subchr(string1,char1,newChar):
    aList=list(string1)
    for i in range(len(string1)):
        if char1==string1[i]:
            aList[i]=newChar
    return ''.join(aList)

if __name__=='__main__':
    print(findchr('alexander','l'))
    print(rfindchar('alexander','a'))
    print(subchr('alexander','a','b'))