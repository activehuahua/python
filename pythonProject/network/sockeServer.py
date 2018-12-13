
# socket server

import socket
import time, threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen(5)
print ('Waiting for connection...')





def tcplink(sock, addr):
    print ('Accept new connection from %s:%s' % (sock, addr))
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break

        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()

    print ('Connection from %s:%s closed' %addr )



while True:
    s, addr = sock.accept()
    t = threading.Thread(target = tcplink, args = (s, addr))
    t.start()