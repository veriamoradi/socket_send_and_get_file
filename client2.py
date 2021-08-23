# client

import socket
import time

# Create an socket object. Family: Internet , Type: TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# My system IP address (127.0.0.1)
host = "127.0.0.1"
# port = int(sys.argv[1])
port = 1888
# Connect to server
addr = (host, port)
mysock.connect(addr)

# Recieve 1024 bytes
c = []
buffer_size = 208400
# print (str(servermsg))
s = mysock.recv(buffer_size).decode('utf-8')
time.sleep(1)
file_name = mysock.recv(buffer_size)
time.sleep(1)
num = int(s)
if num == 0:
    num = 1
with open(file_name.decode('utf-8'), 'wb') as f:
    for i in range(num):
        file_get = mysock.recv(buffer_size)
        f.write(file_get)
print(num * buffer_size)
mysock.close()
print('\nend')

    
    
