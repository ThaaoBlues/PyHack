
import socket
from io import StringIO
from multiprocessing import Process, freeze_support
from subprocess import check_output, STDOUT
import res
import sys
class scanner():
    def __init__(self):

        hostname = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        print("YOU :: {} :: {}".format(hostname,ip))
        base_ip = ip.split(sep=".")
        base = "{}.{}.{}.".format(base_ip[0],base_ip[1],base_ip[2])
        self.scan(base)


    def scan(self,ip):
    
        for i in range(255):
            proc = Process(target= self.ping, args=(ip,i,))
            proc.start()
    def ping(self,ip,i):
            if i == 0:
                pass    
            else:
                cmd = f"ping -c 1 {ip}{i}".split()
                try:
                    r = check_output(cmd, shell=False, stderr = STDOUT)
                    if "1 received" in str(r):
                        print("[{}] {} :: {} ".format(str(i),ip+str(i),str(socket.gethostbyaddr(ip+str(i))[0])))
                except:
                    pass
                



if __name__ == "__main__":
    freeze_support()
    scan = scanner()
