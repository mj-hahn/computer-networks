def application_layer(msg):
	msg = "1" + msg
	print msg
	presentation_layer(msg)
	return
def presentation_layer(msg):
	msg = "1" + msg
	print msg
	session_layer(msg)
	return
def session_layer(msg):
	msg = "1" + msg
	print msg
	transport_layer(msg)
	return
def transport_layer(msg):
	msg = "1" + msg
	print msg
	network_layer(msg)
	return
def network_layer(msg):
	msg = "1" + msg
	print msg
	datalink_layer(msg)
	return
def datalink_layer(msg):
	msg = "1" + msg
	print msg
	physical_layer(msg)
	return
def physical_layer(msg):
	msg = "1" + msg
	print msg
	return

def main(message):
	application_layer(message)
	return

message = raw_input("Please enter a message...\n")
main(message)