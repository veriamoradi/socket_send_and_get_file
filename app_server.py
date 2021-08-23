# server
import os
from tkinter import *
import tkinter.filedialog as tkfile
import socket
import time

file = tkfile.askopenfilename()
if file == '':
    exit('file name is not valid plise inter the file name valide')
with open(file, 'rb')as f :
    image_file= f.read()
file_name = os.basename(file)
x = round(len(image_file)/1024)
temp = image_file

if len(image_file)%1024 < 512: 
    x+=1
    
y = 1024
lis = []
for i in range(x):
    lis.append(temp[:y])
    temp = temp[1024:]
print(len(lis))
for i in lis :
    print(len(i))



# Create an socket object. Family: Internet , Type: TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# My system IP address (127.0.0.1)
host = "127.0.0.1"
port = 9393



# Server Address
addr = (host, port)
mysock.bind(addr)

# queue up to 10 requests
mysock.listen(1)

# with open('seven.png', 'rb') as f :
#     send = f.read()

sendsplit = lis

clientsock, clientaddr = mysock.accept()
print ("connection from: {0}".format(str(clientaddr)))
clientsock.send(str(len(sendsplit)).encode('ascii'))
time.sleep(1)
clientsock.send(file_name.encode('ascii'))
time.sleep(1)
for send_f in sendsplit :
    clientsock.send(send_f)
print('end')
clientsock.close()