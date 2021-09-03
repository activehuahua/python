import  string
dict1,dict5,dict6={},{},{}
dict1['name']='venus'
dict1['port']=6969
dict5={'abc':456}
dict6={'abc':123,98.6:97}
print('host %(name)s is running on port %(port)d'%dict1)

print(dict([('xy'[i-1],i) for i in range(1,3)]))