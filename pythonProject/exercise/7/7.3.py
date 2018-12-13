dict1={'keyB':'B','keyA':'A','keyC':'c'}
list1=list(dict1.keys())
list1.sort()
print(list1)

for eachkey in list1:
    print(eachkey,dict1[eachkey])

list2=list(dict1.values())
list2.sort()
for values in list2:
     for keys in dict1.keys():
         if dict1[keys]==values:
             print(values,'--',keys)
     