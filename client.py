#!/usr/bin/env python2
from socket import *
HOST="localhost"
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpClientSock=socket(AF_INET,SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
    data=raw_input(">")
    if not data:
        break
    tcpClientSock.send(data)
    data=tcpClientSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpClientSock.close()
