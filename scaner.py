#! /usr/bin/python3
from socket import *
def get_host():
    host=input("Enter your start host:")
    ip_scope=int(input("Enter the 'ip scope' (0~255):"))
    port_scope=int(input("Enter the 'port scope'(0~65535)"))
    result={"ip_scope":ip_scope,"host":host,"port_scope":port_scope}
    return result
def scanPort(host,port):
    ss=socket(AF_INET,SOCK_STREAM)
    #print("Scaning [ %s ] port"%host)
    data_file=open("date_file.txt","a+")

    try:
        ss.connect((host,port))
        data_file.write("Scaning [ %s ] port\n[+]%d is open\n"%(host,port))
        print("Scaning [ %s ] port"%host)
        print("[+]%d is open"%port)
        data_file.close()
    except:
        #print("[-]%d is close"%port)
        pass
def main():
    setdefaulttimeout(0.01)
    data=get_host()
    data_host=data["host"]
    for i in range(int(data["host"].split(".")[3]),int(data["host"].split(".")[3])+data["ip_scope"]+1):
        host_l=len(data["host"])
        host3_l=len(data["host"].split(".")[3])
        data_host=data_host[0:host_l-host3_l]
        data_host=data_host+str(i)
        for p in range(data["port_scope"]):
            scanPort(data_host,p)
            #print(data_host)
if __name__=="__main__":
    main()
