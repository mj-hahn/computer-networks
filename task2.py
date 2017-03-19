def generator(message, polynomial):
	# convert binary input to decimal
	message_int = int(message, 2)
	polynomial_int = int(polynomial, 2)
	# find the remainder
	remainder = message_int % polynomial_int
	# convert remainder to binary
	remainder = bin(remainder)
	codeword = str(message) + str(remainder).replace('b','')
	return codeword;

def verifier(message, polynomial):
	print("verifier")
	return

def alter(codeword):
	print("alter")
	return

# main program:
message = raw_input("Please enter a message consisting of 1s and 0s\n")
# check input for validity (should only contain 1s and 0s)
valid = set('01')
if set(message) <= valid:
	# message was valid, continue program
	polynomial = raw_input("Please enter a polynomial for CRC consisting of 1s and 0s\n")
	# check input again
	if set(polynomial) <= valid:
		print(generator(message, polynomial))
	else:
		print("invalid polynomial")
else:
	print("invalid message")
