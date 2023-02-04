import socket
import cv2 as cv
import pickle
import struct


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '10.3.69.34' 
port = 9999
s.connect((host_ip,port)) # a tuple
msg = b""
payload_size = struct.calcsize("Q")
while True:
	while len(msg) < payload_size:
		packet = s.recv(4096) 
		if not packet:
			break
		msg+=packet
	packed_msg_size = msg[:payload_size]
	msg = msg[payload_size:]
	msg_size = struct.unpack("Q",packed_msg_size)[0]
	
	while len(msg) < msg_size:
		msg += s.recv(4096)
	frame_data = msg[:msg_size]
	msg  = msg[msg_size:]
	frame = pickle.loads(frame_data)
	cv.imshow("RECEIVING VIDEO",frame)
	if cv.waitKey(1) == '13':
		break
s.close()
