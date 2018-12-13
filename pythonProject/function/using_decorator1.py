import functools


def log(func):
    """定义一个函数，根据参数类型，决定两层嵌套还是三层嵌套"""
    if callable(func):
    #如果接收的参数是函数，则用两层嵌套
        @functools.wraps(func)
        def myWrapper(*args,**kw):
            """定义一个包装函数，接收任意参数，返回值为要包装的函数的执行结果"""
            print('begin call %s()' % (func.__name__))
            func(*args,**kw)
            print('end call %s()' % (func.__name__))
        return myWrapper

    else:
    #如果接收的参数是字符串，则用三层嵌套
        def decorator(trueFunc):
            @functools.wraps(trueFunc)
            def myWrapper(*args,**kw):
                """定义一个包装函数，接收任意参数，返回值为要包装的函数的执行结果"""
                print('begin %s %s()' % (func,trueFunc.__name__))
                trueFunc(*args,**kw)
                print('end %s %s' % (func,trueFunc.__name__))
            return myWrapper
        return decorator


@log
def f1():
    print('这是F1函数')


@log('excute')
def f2():
    print('这是F2函数')


#if __name__  == '__main__':
f1()
f2()