
# socket server

import socket
import time, threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 19999))


print ('Bind UDP on 999...')
while True:
        data,addr= sock.recvfrom(1024)
        print('Received from %s:%s.' % addr)
        reply = 'Hello, %s!' % data.decode('utf-8')
        sock.sendto(reply.encode('utf-8'), addr)




