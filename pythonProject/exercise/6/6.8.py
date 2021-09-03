import  string
aList_single=['one','two','three','four','five','six','seven','eight','nine']
aList_tens=['ten','twenty','thirty','forty','fifty','sixty','serventy','eighty','ninty']
aList_teens=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']



def deelDigitToEnglish(num):
    listDight=list(num)
    str=''
    if len(listDight)==1:
        str=getOne(num)
    elif len(listDight)==2 :
        str=getTwo(num)
    elif len(listDight)==3 :
        str=getThree(num)
    print(str)

def getOne(num):
    num=int(num)
    if num !=0:
        str=aList_single[num-1]
    return  str

def getTwo(num):
    num=int(num)
    num1=num//10
    num2=num%10
    if num<20 and num>10:
        str=aList_teens[num-11]
    elif num>=20 and num2!=0:
        str=aList_tens[num1-1]+'-'+getOne(num2)
    elif  num>=20 and num2==0:
        str=aList_tens[num1-1]
    else:
        str=aList_tens[0]
    return str


def getThree(num):
    num1=int(num)//100
    num2=int(num)%100
    if num2!=0 and num2>=10:
       str=aList_single[num1-1]+' hundred and '+getTwo(num2)
    elif num2<10:
        str=aList_single[num1-1]+' hundred and '+getOne(num2)
    else:
        str=aList_single[num1-1]+' hundred'
    return str

if __name__=='__main__':
    num=input('Please input a number :')
    while num !='q':
        if not num.isdigit():
            print('Input invalid, please input again!')
            num=input('Please input a number :')
        else:
            # num=int(num)
            deelDigitToEnglish(num)
        num=input('Please input a number :')

