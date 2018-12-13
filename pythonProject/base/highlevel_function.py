import  math
def addord(x,y,f):
    return f(x)+f(y)

print(addord(-3,-4,abs))
print("The value is %.2f"%(addord(3,4,math.sqrt)))

print ("His name is %s"%("Aviad"))