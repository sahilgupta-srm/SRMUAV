import socket
import  cv2
import pickle
import struct
import imutils

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 9999
socket_address = (host_ip,port)
s.bind(socket_address)
s.listen(5)
while True:
	cst,addr = s.accept()
	if cst:
		vid = cv2.VideoCapture(0)
		
		while(vid.isOpened()):
			img,frame = vid.read()
			frame = imutils.resize(frame,width=320)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			cst.sendall(message)
			
			cv2.imshow('TRANSMITTING VIDEO',frame)
			if cv2.waitKey(1) == '13':
				cst.close()