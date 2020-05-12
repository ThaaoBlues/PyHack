import socket
import os
import platform
import threading
from multiprocessing import Process, freeze_support
import sys
from datetime import datetime
import time
class virus_scanner():
    def __init__(self):
        self.socket = ''
        self.base = ''
        self.infected = []
        self.time_past = 0
        self.port = int(input("type the port used by the virus :: "))
        self.scanner()

    def DHCP_thread(self,index):
        print("Thread :: {}".format(index))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        first_index = index
        while index <= first_index+5:
            try:
                sock.connect((str(self.base + str(index)),self.port))
                self.infected.append(str(self.base + str(index)))
            except:
                pass
            index +=1
        sock.close()
        exit(1)

    def wait_message(self):
        pos = 1
        if platform.system() == 'Windows':
            command = "cls"   
        else :
            command = "clear"
        time.sleep(1)
        os.system(command)
        while True:
            if pos == 1:
                sys.stdout.write("\r Processing DHCP scan... | :: time past :: {}s \r".format(self.time_past))
                time.sleep(0.25)
                self.time_past += 0.25
                pos = 2
            elif pos == 2:
                sys.stdout.write("\r Processing DHCP scan... / :: time past :: {}s \r".format(self.time_past))
                time.sleep(0.25)
                self.time_past += 0.25
                pos = 3
            elif pos == 3:
                sys.stdout.write("\r Processing DHCP scan... - :: time past :: {}s \r".format(self.time_past))
                time.sleep(0.25)
                self.time_past += 0.25
                pos = 4
            elif pos == 4:
                sys.stdout.write("\r Processing DHCP scan... \\ :: time past :: {}s \r".format(self.time_past))
                time.sleep(0.25)
                self.time_past += 0.25
                pos = 1
            
    def scanner(self):
        file = open("test.txt","w")
        if platform.system() == 'Windows':
            file = open("test.txt","r")
            os.system("cd {}".format(os.getcwd()))
            os.system("ipconfig >> test.txt")
            
        else :
            file = open("test.txt","r")
            os.system("cd {}".format(os.getcwd()))
            os.system("ifconfig >> test.txt")
            
        file_split = file.read().split(sep = " ")
        last_digit = []
        ip = []
        #select the ipv4 "base" address 
        for ele in file_split:
            if ele.startswith("192."):
                ele_str = str(ele)
                print(len(ele_str)-1)
                if len(ele_str)-1 == 12:
                    self.base = str(ele_str[:-3])
                elif len(ele_str)-1 == 11:
                    self.base = str(ele_str[:-2])
                elif len(ele_str)-1 == 10:
                    self.base = str(ele_str[:-1])
                print(ele_str)
                ip.append(ele_str)
            elif ele.startswith("172."):
                ele_str = str(ele)
                print(len(ele_str)-1)
                if len(ele_str)-1 == 11:
                    self.base = str(ele_str[:-3])
                elif len(ele_str)-1 == 10:
                    self.base = str(ele_str[:-2])
                elif len(ele_str)-1 == 9:
                    self.base = str(ele_str[:-1])
                print(ele_str)
                ip.append(ele_str)
            elif ele.startswith("10."): #idk how to handle this type of addresses
                ele_str = str(ele)
                print(len(ele_str)-1)
                if len(ele_str)-1 == 8:
                    self.base = str(ele_str[:-3])
                elif len(ele_str)-1 == 7:
                    self.base = str(ele_str[:-2])
                elif len(ele_str)-1 == 6:
                    self.base = str(ele_str[:-1])
                print(ele_str)
                ip.append(ele_str)
                
        #display waiting message while scannig
        wait_message = Process(target = self.wait_message)
        wait_message.start()
        time_start = datetime.now()
        index = 0
        t_list = []
        #Dynamically create Threads to divide DHCP scanner IP's range
        for i in range(51):
            thread = threading.Thread(target = self.DHCP_thread, args=(index,))
            t_list.append(thread)
            index += 5
        for thread in t_list:
            thread.start()
        for thread in t_list:
            thread.join()
        #stop wait message an display host infected
        wait_message.terminate()
        print("Began at {}, end at {}, lasted {}s".format(time_start,datetime.now(),self.time_past))
        print("Infected Hosts :: ")
        for host in self.infected:
            print(host)


if __name__ == '__main__':
    freeze_support()     
    virus_scaner1 = virus_scanner()
            
