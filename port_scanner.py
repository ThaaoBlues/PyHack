import socket
from multiprocessing import Process, freeze_support

class port_scanner():
    
    def __init__(self):
        pass

    def scan(self,ip,max=8888):
        print(f"[+] beginning scan... ({max} ports) ")
        for i in range(max):
            proc = Process(target=self.connect, args =(ip,i,))
            proc.start()
    
    def connect(self,ip,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print(f"\r[+]Trying port number {port}", end="")
            sock.connect((ip,port))
            print(f"\r=====[+] OPEN PORT : {port}=====\n",end="")
        except:
            pass


if __name__ == "__main__":
    ps = port_scanner()
    ps.scan(input("IP : "),max=int(input("PORT RANGE : ")))