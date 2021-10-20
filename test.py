print("\033[92m")
import os
import urllib2
import sys 
os.system("figlet web info")
print("\033[91m")
print("Codex by MD Sabbir")
print("\033[93m")
url = raw_input("ENTER WEBSITE LINK : ")
url.rstrip ( )
header = urllib2.urlopen (url) .info ( )
print(str (header) ) 
