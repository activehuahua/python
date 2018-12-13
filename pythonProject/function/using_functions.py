def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(*number):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum

print(calc(1,2,3))

num=[1,2,3]
print(calc(*num))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('alex',42,**extra)

def person(name, age, *,  city, job):
    print(name, age, city, job)

person('alex',40, city='BJ',job='Engineer' )

def fact(n):
    return fact_interate(n,1)

def fact_interate(n,product):
    if n==1:
        return product
    return fact_interate(n-1,n*product)

print(fact(10))

def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)

move(4,'A','B','C')
