import copy
def f(x):
    return  x*x

r=map(f,[1,2,3,4,5,6,7,8,9])

m=copy.deepcopy(r)

print(list(m))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

print(list(r))

a = [1, 2, 3, 4, ['a', 'b']]
a.remove(1)
print(a)
