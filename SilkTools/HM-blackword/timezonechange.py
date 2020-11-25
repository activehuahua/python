#!/usr/bin/python3
# -*-coding:utf-8 -*-

import datetime
#from pytz import timezone
import pytz


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%S+00:00'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    # print(local_dt)
    time_str = local_dt.strftime(local_format)
    return time_str

if __name__ == '__main__':
    time_str=utc_to_local('2018-05-09T14:06:58+02:00')
    print(time_str)