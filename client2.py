# client

import socket
import time
import hashlib

def calclate_hash_sha256(file_path : str) -> hex:
    bufer_sizes = 65536
    sha2 = hashlib.sha256()

    with open(file_path , 'rb') as f:
        while True:
            file = f.read(bufer_sizes)
            if not file:
                break
            sha2.update(file)
    return sha2.hexdigest()

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
file_name = mysock.recv(buffer_size).decode('utf-8')
time.sleep(1)
num = int(s)
if num == 0:
    num = 1
with open(file_name, 'wb') as f:
    for i in range(num):
        file_get = mysock.recv(buffer_size)
        f.write(file_get)
print(num * buffer_size)
hash_file = mysock.recv(1024).decode('utf-8')
mysock.close()
print('\nend\n')
if hash_file == calclate_hash_sha256(file_name):
    print('hash is ok')
else:
    print('hash is not ok')
    
    
