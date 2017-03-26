import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
print 'A: sending HELLO to server'
clientsocket.send('HELLO')

connected = False
filename = 'sample.txt'

# listen for ack
while True:
	buf = clientsocket.recv(64)
	if buf == "ack":
		# successfully connected
		connected = True
		print 'B: ack received'
		# send the name of the file being requested
		print 'C: requesting file from server'
		clientsocket.send(filename)
	if connected == True:
		# receive the contents of the file
		buf = clientsocket.recv(64)
		if len(buf) > 0:
			print 'D: file received from server'
			file_contents = buf
			file = open('destination_folder/sample.txt', 'w')
			file.write(file_contents)
			file.close()
			print 'D: file saved in destination folder'
			break