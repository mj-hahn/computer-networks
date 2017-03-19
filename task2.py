# define functions...
def generator(message, polynomial):
	# find number of digits in polynomial
	length = len(polynomial)
	# convert binary input to decimal. also add length-1 0s
	message_int = int(message+'0'*(length-1), 2)
	polynomial_int = int(polynomial, 2)
	# find the remainder
	remainder = message_int % polynomial_int
	# convert remainder to binary
	remainder = bin(remainder)
	codeword = str(message) + str(remainder).replace('b','')
	return codeword;

def verifier(codeword, polynomial):
	# convert binary input to decimal
	codeword_int = int(codeword, 2)
	polynomial_int = int(polynomial, 2)
	# find the remainder
	remainder = codeword_int % polynomial_int
	# remainder should be 0 if message was valid
	print (remainder)
	return remainder == 0;

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
		# polynomial was valid, continue the program
		# call the generator function
		codeword = generator(message, polynomial)
		print 'Codeword: ', codeword
		print 'Polynomial: ', polynomial
		# pass the codeword into the verifier
		print(verifier(codeword, polynomial))
	else:
		print("Invalid polynomial. Terminating program.")
else:
	print("Invalid message. Terminating program.")
