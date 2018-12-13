from  collections import namedtuple, deque,defaultdict,OrderedDict,Counter

Point= namedtuple('Point',['x','y'])
p=Point(1,2)
print( p.x, p.y)

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(list(q))

dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])

d=dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

d=OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(list(d))

c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c['m'])