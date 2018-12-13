import json

d = dict(name='bob', age=20, score=80)
f= open('json.txt','w')
json.dump(d,f)
f.close()

f=open('json.txt','r')
print(json.load(f))
f.close()


