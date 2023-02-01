import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#to create socket object ipv4 and TCP 
s.bind((socket.gethostname(),5050))#5050 is the port number
s.listen(5)#To make a queue
while True:
    cst,add=s.accept()#cst stores object,add is their IP address
    print(f"Connection from {add} has been established")
    cst.send(bytes("Welcome to the server!","utf-8"))#for sending information
    cst.close()
