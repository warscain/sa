#!/usr/bin/env python
# -*- coding: UTF-8 *-*
#import sys
#import socket
#serverHost = 'localhost'
#serverPort = 50007
#
#message = ['Hello network world', 'twice', '3333333', "444444"]
#
#if len(sys.argv) > 1:
#    serverHost = sys.argv[1]
#    if len(sys.argv) > 2:
#        message = sys.argv[2:]
#
#TcpCliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#TcpCliSocket.connect((serverHost, serverPort))
#
#for line in message:
#    TcpCliSocket.send(line)
#    data = TcpCliSocket.recv(1024)     #从服务端接收到的数据，上限为1k
#    print 'Client received:', repr(data)
#
##关闭套接字
#TcpCliSocket.close()

# out >>>
#Client received: 'Echo=>Hello network world'
#Client received: 'Echo=>twice'
#Client received: 'Echo=>3333333'
#Client received: 'Echo=>444444'


import sys
import socket
serverHost = 'localhost'
serverPort = 50007

message = ['Hello network world', 'twice', '3333333', "444444"]

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = sys.argv[2:]

TcpCliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TcpCliSocket.connect((serverHost, serverPort))

while True:
    TcpCliSocket.send(raw_input('>'))
    data = TcpCliSocket.recv(1024)     #从服务端接收到的数据，上限为1k
    print 'Client received:', repr(data)

#关闭套接字
TcpCliSocket.close()


























