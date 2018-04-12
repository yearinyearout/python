#!/usr/bin/env python2
from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
tcpServerSock=socket(AF_INET,SOCK_STREAM)
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)

while True:
    print "waiting for connect..."
    tcpClientSock,addr=tcpServerSock.accept()
    print "Connected from:",addr

    while True:
        data=tcpClientSock.recv(BUFSIZ)
        if not data:
            break
        tcpClientSock.send('[%s] %s'%(ctime(),data))



    tcpClientSock.close()
