shoplist=['apple','mango','carrot','banana']
print('I have ',len(shoplist),'items to purchase.')

shoplist.append('watermillon')
for item in shoplist :
    print( item,end=' ' )
print('\n')
shoplist.sort()

print(shoplist,end='\n')

del  shoplist[0]

print(shoplist)