'''

Task 2: Implement the Internet Checksum Algorithm

Checksum Algorithm:

	1)
		compute the decimal sum of each word in the bit stream
		e.g. 2 words, 1100 and 1010
			 sum = 12 + 10 = 22
	2) 
		determine the modulo value.
		moduloValue = 2^(# bits per word) - 1
		In the example above, moduloValue = 15, because the message
		consisted of two 4 bit words, and 2^4 - 1 = 15. 
	
	3)
		compute X, where
		X = sum modulo (moduloValue)
		
	4)
		compute bL, where
		bL = -X
		
	5)
		compute:
			bL modulo (moduloValue)
			
	6) 
		compute:
			result = (sum + bL) modulo (moduloValue)
		
		if result = 0
			the checksum is satisfied
		else
			the checksum is not satisfied
	
'''

import sys

''' 
	check input for validity. Valid inputs must:
		-Only contain 1s and 0s
		-Be 8 bytes (32 bits)
'''
def checkBitStream(bitstream):

	valid = set('01')
	if (set(bitstream) <= valid) and (len(bitstream) == 32):
		return True 
	
	return False
	
def binaryToDecimal(byte):
	
	sum = 0
	for bit in range(3, -1, -1):
		
		if byte[bit] == '1':
			p = 3 - bit
			sum += pow(2,p)
		
	return sum
	
def decimalToBinary(num):

	checkSum = ''
	count = num

	if ( count >= pow(2,3) ):
		checkSum  += '1'
		count -= 8
	else:
		checkSum  += '0'
		
	if ( count >= pow(2,2)  ):
		checkSum += '1'
		count -= 4
	else:
		checkSum  += '0'
		
	if ( count >= pow(2,1)  ):
		checkSum += '1'
		count -= 2
	else:
		checkSum  += '0'
	
	if ( count >= pow(2,0)  ):
		checkSum += '1'
		count -= 1
	else:
		checkSum  += '0'

	return checkSum
	
def getCheckSum(message):
	# compute the decimal sum of each word in the bit stream
	sum = 0
	for num in range(0,8):
	
		byte = message[4*num + 0] + message[4*num + 1] + message[4*num + 2] + message[4*num + 3]
		sum += binaryToDecimal(byte)		
	
	# determine the modulo value
	moduloValue = 4
	
	#compute X, where X = sum modulo (moduloValue)
	X = sum % moduloValue
	
	# compute bL, where bL = -X
	bL = X*(-1)
	
	return bL

def generator():

	'''
	# get user input
	message = raw_input("Please enter a message consisting of 1s and 0s\n")
	check = checkBitStream(message)
	if check != True:
		print("Invalid message")
		sys.exit(0)
	'''
	message = '11111111100001111000111111111111'
	print "message is:", message
	
	return message	

def verifier(message, bL):

	# compute the decimal sum of each word in the bit stream
	sum = 0
	for num in range(0,8):
	
		byte = message[4*num + 0] + message[4*num + 1] + message[4*num + 2] + message[4*num + 3]
		sum += binaryToDecimal(byte)	

	moduloValue = 4
	
	# compute: bL modulo (moduloValue)
	checksumDecimal = bL % moduloValue
	checksum = decimalToBinary(checksumDecimal)
	
	# compute: result = (sum + bL) modulo (moduloValue)
	result  = (sum + bL) % moduloValue
	if (result == 0):
		print "the checksum is satisfied"
	else:
		print "the checksum is NOT satisfied"
	
	return

def alter(message):

	print "\n"
	altered = message
	if (altered[30] == '1'):
		altered = altered[:30] + '0' + altered[31:] 
	else:
		altered = altered[:30] + '1' + altered[31:] 
		
	print "Altered bitstream:", altered
	return altered

	
def main():
	
	# Not altered
	message = generator()
	checkSum = getCheckSum(message)
	verifier(message, checkSum)
	
	# Altered
	alteredMessage = alter(message)
	verifier(alteredMessage, checkSum)
	
	return

if __name__ == "__main__":
	print "\n"
	main()
	print "\n"
	sys.exit(0)