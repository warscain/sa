#!/usr/bin/env python
# -*- coding: UTF-8 *-*



from socket import *
#HOST='localhost'
HOST="192.168.1.100"
PORT=21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()

