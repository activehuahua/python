import time,threading

locka = threading.Lock()
lockb = threading.Lock()

def fa():
    print('a')
def fb():
    print('b')

def fab():
    locka.acquire()
    try:
        fa()
        time.sleep(1)
        lockb.acquire()
        try:
            fb()
        finally:
            lockb.release()
    finally:
        locka.release()
def fba():
    lockb.acquire()
    try:
        fb()
        time.sleep(1)
        locka.acquire()
        try:
            fa()
        finally:
            locka.release()
    finally:
        lockb.release()

t1 = threading.Thread(target=fab)
#t2 = threading.Thread(target=fab)
t1.start()
#t2.start()
t1.join()
#t2.join()
print('end')