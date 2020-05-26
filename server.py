from socket import *
from time import *

HOST = ''
PORT = 8000
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        print(data.decode('utf-8'))
        if not data:
            break
        tcpCliSock.send(bytes('200', 'utf-8'))
    tcpCliSock.close()
tcpSerSock.close()