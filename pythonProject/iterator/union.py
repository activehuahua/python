import copy
aa=set([])
a = ['a', 'b', 'c', 'd']
b = ['c', 'x', 'g', 'h']
c = ['1', 'as', 'ci', 'v']
d = ['1', '2', '3', '4']

aa=list(aa.union(a, b, c, d))
print(aa)
bb=copy.deepcopy(aa)

bb.sort()
print(aa)
print(bb)

aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort();
print("List : ")
print(aList)