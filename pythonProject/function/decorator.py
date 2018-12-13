
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-04-23')

@log
def now1():
    print('2018-04-23 14:12')
now()
now1()