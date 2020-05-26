from socket import *

HOST = '3.133.100.99'
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('Please input data :')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    
    data1 = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data1.decode('utf-8'))

tcpCliSock.close()