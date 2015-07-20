#Simple encryption schema taught in class
#βάζει ένα σικουενς από 0 1 και κάνει ενκρυπτ με το κλειδί
#με την ίδια κάνεις και ανενκριπτ  
def encrypt( key , byte):
	key = str(key);byte = str(byte);
	assert len (key)== len ( byte )
	w = [];s="";
	for i in range(len(key)):
		w.append((int(byte[i]) + int(key[i])) % 2 )
	for i in range(len(w)):
		s = s + str(w[i])
	return s
#the same function deciphers the message if the key is known
