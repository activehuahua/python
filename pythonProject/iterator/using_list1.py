from collections import Iterable
import os
L=list(range(1,11))
print(L[:])

d={'a':1,'b':2,'c':3}
for k,v in d.items():
    print(k,v)

for i,value in enumerate(['a','b','c']):
    print(i,value)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x,y)

print([x*x for x in list(range(1,11)) if x%2==0])

print([m+n for m in 'abc' for n in 'xyz'])

print([d for d in os.listdir('.')])

g=(x*x for x in range(10))

for n in g:
    print(n)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

for n in fib(6):
    print(n)