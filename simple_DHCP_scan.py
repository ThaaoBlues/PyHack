
import socket
from io import StringIO
from multiprocessing import Process, freeze_support
from subprocess import check_output, STDOUT
import port_scanner
import res
import sys

class scanner():
    def __init__(self):

        open("hosts.log","w")
        hostname = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        base = s.getsockname()[0]
        print("YOU :: {} :: {}".format(hostname,base))
        base = base.split(sep=".")
        base = "{}.{}.{}.".format(base[0],base[1],base[2])
        self.hosts = []
        self.scan(base)

    def scan(self,ip):
    
        for i in range(255):
            proc = Process(target= self.ping, args=(ip,i,))
            proc.start()
            if i == 254:
                proc.join()

        a = input("[+]Do you wanna try a port scan on the hosts ?[y/n]")

        if "y" in a:

            with open("hosts.log","r") as f:
                for line in f.read().split("\n"):
                    self.hosts.append(line)
            
            r = int(input("PORT RANGE : "))
            for host in self.hosts:
                ps = port_scanner.port_scanner()
                ps.scan(host,max= r)
        else:
            print("BYE !")

    def ping(self,ip,i):
        if i == 0:
            pass    
        else:
            cmd = f"ping -c 1 {ip}{i}".split()
            try:
                r = check_output(cmd, shell=False, stderr = STDOUT)
                if "1 received" in str(r):
                    with open("hosts.log","a") as f:
                        f.write(ip+str(i)+"\n")
                    print("[{}] {} :: {} ".format(str(i),ip+str(i),str(socket.gethostbyaddr(ip+str(i))[0])))
            except:
                pass
        
                
