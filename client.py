import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#to create socket object ipv4 and TCP 
s.connect((socket.gethostname(),5050))
msg=''
while True:
    temp=s.recv(64)
    if len(msg)<=0:
        break
    msg+=temp.decode("utf-8")
print(full_msg)