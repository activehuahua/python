import itertools

na=itertools.repeat('alex',3)
for n in na:
    print(n)


natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
for n in ns:
    print(n)

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

