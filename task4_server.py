import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

connected = False

# listen for hello
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    # listen for client
    if buf == "HELLO":
    	connected = True
    	print 'A: HELLO received'
    	# client wants to connect, send an ack
    	print 'B: sending ack'
    	connection.send('ack')
	# listen for file request (after connected)
	buf = connection.recv(64)
	if connected == True:
		# if client has sent a filename
		if len(buf) > 0:
			filename = buf
			print 'C: client has requested ', filename
			# read the file requested and send the contents to the client
			file = open('source_folder/'+filename, 'r')
			file_contents = file.read()
			connection.send(file_contents)
			print 'D: file sent to client'
			file.close()
			break
