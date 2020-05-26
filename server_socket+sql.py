from socket import *
from time import *
import pymysql
from datetime import *

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
    data = tcpCliSock.recv(BUFSIZ)
    tcpCliSock.send('200'.encode('utf-8'))
    stx = data[0]
    etx = data[-1]

    print(data.decode('utf-8'))
    if not data:
        break
    if stx == '[' and etx == ']':
        conn = pymysql.connect(
        host = '3.133.100.99',
        user ='kang851216',
        passwd = 'rkdrudals1',
        db='RAWDATA',
        charset='utf8mb4',)
        dt = data.decode('utf-8')
        rawdata = dt.split(',')
        machinenoi = rawdata[0][1:]
        QRcodei = rawdata[1]
        weighti = rawdata[2][1:]
        stati = rawdata[-1]
        doorstati = stati[0]
        hopperstati = stati[1]
        datei = datetime.now().strftime("%Y") + "-" + datetime.now().strftime("%m") + "-" + datetime.now().strftime("%d")
        timei = datetime.now().strftime("%H") + ":" + datetime.now().strftime("%M") + ":" + datetime.now().strftime("%S")
        cursor = conn.cursor()
        sql= """INSERT INTO data(date, time, machineno, QRcode, weight, doorstat, hopperstat) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (datei, timei, machinenoi, QRcodei, weighti, doorstati, hopperstati))
        conn.commit()
        cursor.close()
    print('Connection complete...')