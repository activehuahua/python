import string
def upper_lower(str1):
    aList=[]

    for i in range(len(str1)):
        if str1[i].isalpha():
            if  str1[i].islower():
                str_temp=str1[i].upper()
                aList.append(str_temp)
            else:
                str_temp=str1[i].lower()
                aList.append(str_temp)
        else:
            aList.append(str1[i])
    str2=''.join(aList)
    print(str2)

def doCapitcal(s):
    str=s.upper()
    print(str)

if __name__=='__main__':
    str_input=input('Please input a string: ');
    while True:
        if str_input =='q':
           break
        else:
            # upper_lower(str_input)
            doCapitcal(str_input)
        str_input=input('Please input a string: ');