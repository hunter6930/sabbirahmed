print("\033[92m")
import os
import urllib2
import sys
os.system("pkg install figlet")
os.system("clear")
os.system("figlet WEB INFO")
print("\033[91m")
print("Codex by AI-22")
print("\033[93m")
url = raw_input("ENTER WEBSITE LINK : ")
url.rstrip ( )
header = urllib2.urlopen (url) .info ( )
print(str (header) )
