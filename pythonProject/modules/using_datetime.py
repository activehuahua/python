from datetime import datetime, timedelta

now=datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())

t=1429417220.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))   # Mon,Sep 13 17:10

now=datetime.now()
dt=now+timedelta(days=1)
print(dt)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
cday=cday+timedelta(hours=-9)

print(cday)