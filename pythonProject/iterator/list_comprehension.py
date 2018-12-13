listone=[2,3,4]
listtwo=[2*i for i in listone if i>2]
print(listtwo)

def powersum(power,*args):
    total=0
    for i in args:
        total+=pow(i,power)
    return total

print(powersum(2,3,4))
print(powersum(2,10))

exec('print("Hello World")')