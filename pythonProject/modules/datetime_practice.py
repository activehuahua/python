import re
from datetime import datetime, timezone, timedelta
import re

def to_timestamp(dt_str, tz_str):
   m=re.match(r'^UTC([+|-]\d{1,2}):(\d+)',tz_str)
  # print(int(m.group(1)))
   zoneHours=int(m.group(1))

   newDay=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
   #newDay=newDay+timedelta(hours=zoneHours)
   tz_utc=timezone(timedelta(hours=zoneHours))
   newDay=newDay.replace(tzinfo=tz_utc)
   #print(newDay.timestamp())
   return newDay.timestamp()


# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')