import math

def quadratic(a,b,c):
    xx=[]
    try:
        xx.append((-b+math.sqrt(b*b-4*a*c))/(2*a))
        xx.append((-b-math.sqrt(b*b-4*a*c))/(2*a))
        return  xx
    except Exception as ex:
        print(ex)

print(quadratic(2,3,1))

def enroll(name,gender,age=20,city='Chengdu'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('alexander','M')
enroll('Alice','F',city='Beijing')