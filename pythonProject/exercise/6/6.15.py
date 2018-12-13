import datetime

d1=datetime.datetime.strptime('2017-07-10 09:00:00','%Y-%m-%d %H:%M:%S')
d2=datetime.datetime.strptime('2017-07-20 09:00:00','%Y-%m-%d %H:%M:%S')

delta=d2-d1

print(delta.days)

birth=datetime.datetime.strptime('1973-08-15 09:00:00','%Y-%m-%d %H:%M:%S')
now=datetime.datetime.now()
print((now-birth).days)

d0='2017-07-10'
d0=datetime.datetime.strftime('%Y-%m-%d')
print(d0)