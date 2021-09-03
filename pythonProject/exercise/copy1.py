import  copy

person = ['name', ['money', 100]]
hubby = person
wifey=list(person)
wifey2 = copy.deepcopy(person)

hubby[0] = 'Joe'
wifey[0]='Jane'
wifey2[0] = 'Jane2'

hubby[1][1] = 20
print(hubby,wifey, wifey2)
print(id(hubby),id(wifey),id(wifey2))