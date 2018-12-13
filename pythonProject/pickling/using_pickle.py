import  pickle

d=dict(name='bob', age=20, score=80)
print(pickle.dumps(d))

f = open('pickling.txt', 'wb')
pickle.dump(d,f)
f.close()

f=open('pickling.txt','rb')
storedlist=pickle.load(f)
f.close()
print(storedlist)