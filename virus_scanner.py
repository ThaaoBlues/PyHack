import socket
import os
import platform
import threading
from multiprocessing import Process, freeze_support
import sys
from datetime import datetime
import time
class virus_scanner():
    def __init__(self,port):
        self.socket = ''
        self.base = ''
        self.infected = ""
        self.time_past = 0
        f = open("pwned_hosts.log","w")
        f.close()
        self.port = port
        self.scanner()


    def DHCP_thread(self,index,base):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((str(base + str(index)),self.port))
            with open("pwned_hosts.log","a") as f:
                f.write(str(base + str(index) + "\n"))
                f.close()
        except:
            pass
        sock.close()
        exit(1)


    def scanner(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        base = s.getsockname()[0]
        base = base.split(sep=".")
        base = "{}.{}.{}.".format(base[0],base[1],base[2])
                

        #Dynamically create processes to divide DHCP scanner IP's range
        for i in range(255):
            proc = Process(target = self.DHCP_thread, args=(i,base,))
            proc.start()
        #stop wait message 


        
        with open("pwned_hosts.log","r") as f:
            self.infected = f.read()
            f.close()

        #display host infected    
        print("Infected Hosts :: ")
        print(self.infected)

    def get_ihosts(self):
        hosts = []
        with open("pwned_hosts.log","r") as f:
            hosts = f.read().split('\n')
            f.close()

        return hosts
            
            
