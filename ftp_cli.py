#!/usr/bin/env python3
from ftplib import FTP
ftp=FTP()
bufsize=1024
def get_user():
    usr_name=input("Enter user name:")
    usr_passwd=input("Enter user password:")
    usr_dict={"usr_name":usr_name,"usr_passwd":usr_passwd}
    return usr_dict
def get_command():
    command_1=input("Enter your command(Enter quit to break):")
    return command_1
def get_ip():
    host=input("Enter the ip of the FTPServer:")
    port=int(input("Enter the port of the FTPServer:"))
    ip_dict={"host":host,"port":port}
    return ip_dict
def main():
    ip_dict=get_ip()
    host=ip_dict["host"]
    port=ip_dict["port"]
    try:
        ftp.connect(host,port)
        print("Connetcted %s "%host)
    except:
        print("[-]Error: Refused ")
        return
    usr_dict=get_user()
    usr_name=usr_dict["usr_name"]
    usr_passwd=usr_dict["usr_passwd"]
    try:
        ftp.login(usr_name,usr_passwd)
        print("Login:",usr_name)
    except:
        print("[-]Error:The account is not find or password is falt.")
        ftp.quit()
        return
    while True:
        command=get_command()
        if command=="dir":
            ftp.dir()
        elif command=="pwd":
            ftp.pwd()
        elif command=="retrbinary":
            filename=input("Enter download file name: ")
            object_file=input("Enter object file name: ")
            file=open(object_file,"wb").write
            ftp.retrbinary("RETR %s"%filename,file,bufsize)
            file.close()
        elif command=="storbinary":
            filename_s=input("Enter object file name: ")
            upload_file=input("Enter upload file name: ")
            file_s=open("/home/king/FTP_CLIENT/"+filename_s,"rb")
            ftp.storbinary("STOR %s"%upload_file,file_s,bufsize)
            file_s.close()
        elif command=="help":
            help(ftp)
        elif command=="quit":
            break
if __name__=="__main__":
    main()
