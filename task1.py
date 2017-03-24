def application_layer(msg):
	msg_in_bits = ""
	for c in msg:
		# convert each letter to ascii
		ascii_number = ord(c)
		# convert each ascii to an 8-bit word (pad with zeros)
		eight_bits = '{:08b}'.format(ascii_number)
		msg_in_bits += eight_bits
	print msg_in_bits
	presentation_layer(msg_in_bits)
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