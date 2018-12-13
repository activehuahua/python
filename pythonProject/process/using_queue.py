from multiprocessing import Process,Queue
import  os,time,random

def write(q):
    print('Process to write %s' %os.getpid())
    for value in ['A','B','C']:
        print('Input Queue：%s' %value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from the queue.'%value)

if __name__=='__main__':
    q=Queue()
    qw=Process(target=write,args=(q,))
    qr=Process(target=read,args=(q,))
    qw.start()
    qr.start()
    qw.join()
    qr.terminate()