import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n=int(s)
    #assert n!=0 ,'n is zero'
    logging.info('n = %d' % n)
    print(10/n)


foo('0')