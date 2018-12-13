import copy
a = [1, 2, 3, ['a', 'b']]
b = copy.copy(a)
c = copy.deepcopy(a)
d = a
a[0] = 0
print(a)
print(b)
print(c)
b[3].append('c')
c[3].append('d')
print(a)
print(b)
print(c)
b.append(5)
c.append('python')
print(a)
print(b)
print(c)