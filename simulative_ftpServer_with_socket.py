#!/usr/bin/env python3
from socket import *
import os
from time import ctime
Host=""
Port=12345
buffsize=1024
Addr=(Host,Port)
server_fd=socket(AF_INET,SOCK_STREAM)
server_fd.bind(Addr)
server_fd.listen(5)

while True:
    print("Wating for connect")
    try:
        client_fd,client_addr=server_fd.accept()
    except:
        print("Accept Error")
    print("{0}\tConnecting to {1}".format(ctime(),client_addr))
    #client_fd.sendall("Please login your account:".encode())
    print("{0}\tWating for recive".format(ctime()))
    user=client_fd.recv(buffsize).decode()
    user=user.split(" ")
    username=user[0]
    password=user[1]
    if username!="root" or password!="989898" :
        break
    print("{0}\tuser:{1} is operating ".format(ctime(),username))
    client_fd.sendall("Please enter your cmd:".encode())
    while True:
        cmd=client_fd.recv(buffsize).decode()
        if cmd=="put":
            data=client_fd.recv(buffsize).decode()
            print("{0}\tuser:{1} is uploading{2}".format(ctime(),username,data))
            data=data.split(" ")
            address=data[0]
            filename=data[1]
            filesize=data[2]
            client_fd.send("200".encode())
            recivesize=0
            file=open(filename,"wb")
            while recivesize<int(filesize):
                filedata=client_fd.recv(buffsize)
                file.write(filedata)
                recivesize+=len(filedata)
            else:
                file.close()
                print("{0}\tfinished!".format(ctime()))
        elif cmd=="dir":
            data=os.listdir()
            for i in data:
                client_fd.send((i+"\n").encode())
        elif cmd=="get":
            filename=client_fd.recv(buffsize).decode()
            filesize=str(os.path.getsize(filename))
            client_fd.send(filesize.encode())
            file=open(filename,"rb")
            for lines in file:
                client_fd.send(lines)
            else:
                print("{0}\tfinished!".format(ctime()))

    client_fd.close()
