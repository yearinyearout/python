#!/usr/bin/env python3
from socket import *
import getpass
import scaner
import os
def login():
    username=input("<Username:")
    password=getpass.getpass("<password")
    usr={"username":username,"password":password}
    return usr
def dir():
    client_fd.send("dir".encode())
def put():
    address=input("Please enter your file address:")
    filename=input("Please input filename:")
    file=open("%s/%s"%(address,filename),"rb")
    filesize=os.path.getsize("%s/%s"%(address,filename))
    data=address+" "+filename+" "+str(filesize)
    print(data)
    client_fd.send(data.encode())
    client_fd.recv(buffsize)
    for lines in file:
        client_fd.send(lines)
    else:
        print('file send is finish')
def get():
    filename_1=input(">filename:")
    client_fd.send(filename_1.encode())
    filesize=client_fd.recv(buffsize).decode()
    file=open(filename_1,"wb")
    filesize_1=0
    while filesize_1<int(filesize):
        filedata=client_fd.recv(buffsize)
        file.write(filedata)
        filesize_1+=len(filedata)
    else:
        file.close()
        print("finished!")


command=input("Enter your command:")
if command=="scaner":
    scaner.scan()
else:
    pass
Addr=input("Please Enter the hostaddress and Port(x.x.x.x:Port) :")
Host=Addr.split(":")[0]
Port=int(Addr.split(":")[1])
buffsize=1024
Hostaddress=(Host,Port)
#print Hostaddress
client_fd=socket(AF_INET,SOCK_STREAM)
try:
    client_fd.connect(Hostaddress)
    print("connection is sucesseful!")
    while True:
        command=input("Please enetr your command:")
        if command=="help":
            os.system("cat help")
        if command=="login":
            usr_dict=login()
            #print(usr_dict)
            usrname=usr_dict["username"]
            password=usr_dict["password"]
            data=usrname+" "+password
            client_fd.send(data.encode())
            data=client_fd.recv(buffsize).decode()
            print(data)
            while True:
                command_1=input("Enter command_1:")
                if command_1=="dir":
                    dir()
                    data=client_fd.recv(buffsize).decode()
                    print(data)
                elif command_1=="put":
                    client_fd.send("put".encode())
                    put()
                elif command_1=="get":
                    client_fd.send("get".encode())
                    get()
                elif command_1=="quit":
                    break
        elif command=="quit":
            break
    client_fd.close()

except :
    print("connection is failed!")
