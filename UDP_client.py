#!/usr/bin/env python
# -*- coding: UTF-8 *-*
from socket import *

HOST = ''
PORT = 50007
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()  