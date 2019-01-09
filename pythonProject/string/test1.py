def make_great(magicians):
    for name in range(0,len(magicians)):
        magicians[name]='the great '+magicians[name].title()

magiccians=['a','b','c']
make_great(magiccians)
print(magiccians)