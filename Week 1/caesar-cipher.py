#This is a python program to encrypt a text with the caesar's encrypting algorithm
#The key is an integer which specifies the radius at which each letter will be moved
#Although simple at Caesar's times most people were illiterate
#If key = 4 then 'Z'------>'D','A' ----->'E' etc
def caesar( text , key ):
	#text is a string we need to split
	L = text.split()
	ascii = []
	for x in L:
		for i in range(len(x)):
			ascii.append( ord(x[i]) )
			#At this point we entered a text i.e. "Xanthippi's dream!"
			#as an output we get a list with the ascii character mapping
			#ascii =[88,97,110, 116, 104,105,112,112,105,39,115,100,114,101,97,109,33]
	#we are going to use the key encryption, remember that the alphabet chars are
	#between ord('A') = 65 and ord('Z') = 90
	#and ord('a') =  97 and ord('z') = 122
	for ii in range(len(ascii)):
		if ascii[ii]>=65 and ascii[ii]<=90:
			ascii[ii] = ascii[ii] - 65
			ascii[ii] = ( ascii[ii] + key ) % 26
			ascii[ii] = ascii[ii] + 65
		if ascii[ii] >= 97 and ascii[ii] <= 122:
			ascii[ii] = ascii[ii] -97
			ascii[ii] = ( ascii[ii] + key ) % 26
			ascii[ii] = ascii[ii] + 97
	#Now we are ready to turn ascii to characters to create the cipher text
	cipher_text = "" #empty string
	for ii in range(len(ascii)):
		ascii[ii] = chr(ascii[ii])
		cipher_text += ascii[ii]
	
	return cipher_text

#>>caesar( "Xanthippi's dream!" , 4  )
#           "Berxlmttm'wHvieq" 
#--------------------------------------------------------------------------------------------------
