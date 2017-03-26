import random

def application_layer(msg):
	msg_in_bits = ""
	for c in msg:
		# convert each letter to ascii
		ascii_number = ord(c)
		# convert each ascii to an 8-bit word (pad with zeros)
		eight_bits = '{:08b}'.format(ascii_number)
		msg_in_bits += eight_bits
	presentation_layer(msg_in_bits)
	return
def presentation_layer(msg):
	# choose a protocol (telnet)
	pres_header = get_random_header()
	msg = pres_header + msg
	session_layer(msg)
	return
def session_layer(msg):
	# choose a protocol (rpc)
	sesh_header = get_random_header()
	msg = sesh_header + msg
	transport_layer(msg)
	return
def transport_layer(msg):
	# assume port 20 (00010100)
	tr_header = "00010100" + get_random_header()
	msg = tr_header + msg
	network_layer(msg)
	return
def network_layer(msg):
	# assume IP address of 10.217.204.85
	# (equivalent to 00001010 11011001 11001100 01010101)
	net_header = get_random_header() + "00001010110110011100110001010101"
	msg = net_header + msg
	datalink_layer(msg)
	return
def datalink_layer(msg):
	# use bit stuffing
	# placing a 0 after 5 consecutive 1s is a simple find and replace
	msg.replace('11111', '111110')
	# add header
	msg = get_random_header() + msg
	physical_layer(msg)
	return
def physical_layer(msg):
	print msg
	print "size: ", len(msg)
	return

def main(message):
	application_layer(message)
	return

def get_random_header():
	header = ""
	# generate a random 32-bit header
	for i in range(0, 32):
		header += str(random.choice([0,1]))
	return header;

message = raw_input("Please enter a message...\n")
main(message)