import hashlib

ssid = raw_input("Enter new SSID: ") 
user_password = raw_input("Enter new Wi-Fi password: ")
salt_string = "ToMarsAndBack"                              #Longer string might make hashing harder

def capitalize(s):                                         #To capitize every other letter in the hash.
	ret = ""
	i = True  
	for char in s:
		if i:
			ret += char.upper()
		else:
			ret += char.lower()
		if char != ' ':
			i = not i
	return ret

#salted_password = user_password+salt_string+ssid           #Adding SSID to prevent rainbow tables.
#hashed_password = hashlib.sha512(salted_password)
#router_password = capitalize(hashed_password.hexdigest())[:63]  #Use longer string if needed.

router_password = capitalize((hashlib.sha512(user_password+salt_string+ssid)).hexdigest())[:63]

print ("\n"*4 + "The password you entered (" + str(len(user_password)) + " char long) :\n" + '\033[91m' + user_password + '\033[0m' + "\n"*2 + "The password the router is going to use (" + str(len(router_password)) + " char long) :\n" + '\033[91m' + router_password )