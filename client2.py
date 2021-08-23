# client

import socket

# Create an socket object. Family: Internet , Type: TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# My system IP address (127.0.0.1)
host = "127.0.0.1"
port = 9393

# Connect to server
addr = (host, port)
mysock.connect(addr)

# Recieve 1024 bytes
c = []
lis = range(7)

# print (str(servermsg))
s = mysock.recv(1024)
file_name = mysock.recv(1024)
for i in range(int(s)):
    servermsg = mysock.recv(1024)
    c.append(servermsg)
mysock.close()
print('end')

with open(file_name, 'wb') as f:
    for i in c:
        f.write(i)
    
    
