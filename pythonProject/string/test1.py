def make_great(magicians):
    for name in range(0,len(magicians)):
        magicians[name]='the great '+magicians[name].title()

# magiccians=['a','b','c']
# make_great(magiccians)
# print(magiccians)

import itertools
counts=[0]*5
a1 = [1, 1, 4, 1]

for num in a1:
    counts[num]+=1
counts=list(itertools.accumulate(counts))
print(counts)