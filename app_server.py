# server
import os
from tkinter import *
import tkinter.filedialog as tkfile
import socket
import time
import hashlib

def open_file():
    tk = Tk()
    file = tkfile.askopenfilename().encode('utf-8')
    tk.destroy()
    print(file)
    if file == '':
        exit('file name is not valid plise inter the file name valide')
    with open(file, 'rb')as f :
        contact_file= f.read()
    return file,contact_file

file, contact_file = open_file()

def str_to_path(file):
    file_name = os.path.normpath(file)
    file_name = os.path.basename(file_name)
    return file_name

file_name = str_to_path(file)

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

def send_file(file_name: str, contact_file:bytes, file_path:str, host:str = '127.0.0.1', port:int = 1888, buffer_size:int = 208400):
    "create an conecion and send len file , name file , file to client"

    x = round(len(contact_file)/buffer_size)
    temp = contact_file
    if x == 0:
        x = 1
    if len(contact_file)%buffer_size < 512: 
        x+=1
    # calclate_hash_sha256
    hash_file = calclate_hash_sha256(file_path)

    # Create an socket object. Family: Internet , Type: TCP
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server Address
    addr = (host, port)
    mysock.bind(addr)
    # queue up to 10 requests
    mysock.listen(1)

    print('start')
    clientsock, clientaddr = mysock.accept()
    print ("connection from: {0}".format(str(clientaddr)))
    clientsock.send(str(x).encode('utf-8'))
    time.sleep(1)
    clientsock.send(file_name)
    time.sleep(1)

    for i in range(x):
        clientsock.send(temp[:buffer_size])
        temp = temp[buffer_size:]
    print('bytes send : ', len(contact_file))

    clientsock.send(hash_file.encode('utf8'))
    clientsock.close()

send_file(file_name, contact_file, file_path= file)