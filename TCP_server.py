#!/usr/bin/env python
# -*- coding: UTF-8 *-*
import socket
myHost = ''             #''代表服务器为localhost
myPort = 50007          #在一个非保留端口号上进行监听

TcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #设置一个TCP socket对象
TcpSerSocket.bind((myHost, myPort))          #绑定它至端口号
TcpSerSocket.listen(5)                       #监听，允许5个连结


while True:                             #直到进程结束时才结束循环
    TcpCliSocket, address = TcpSerSocket.accept()             #等待下一个客户端连结
    print 'Server connected by', address                #连结是一个新的socket

    while True:
        data = TcpCliSocket.recv(1024)
        if not data: break                              #如果没有数量的话，那么跳出循环
        TcpCliSocket.send('Echo=>' + data)
    #当socket关闭时eof
    TcpCliSocket.close( )

#out >>> Server connected by ('127.0.0.1', 56830)


















