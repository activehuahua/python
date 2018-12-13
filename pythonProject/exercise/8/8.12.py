def outputValues(num1,num2):
    print('%15s%15s%15s%15s%15s'%('DEC','BIN','OCT','HEX','ASCII'))
    print(80*'-')
    for i in range(num1,num2+1):
        print('%15s%15s%15s%15s%15s'%(i,bin(i)[2:],oct(i)[2:],hex(i)[2:],chr(i)))

if __name__=='__main__':
    num1=25
    num2=41
    outputValues(num1,num2)
