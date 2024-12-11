def ceaser_CryptographyEncrypted(message, number):
	if(number < 0 and number > 26):
		ceaser_CryptographyEncrypted()
	
	encryptedtext = ' '
	for char in message:
		if(char.isupper()):
			encryptedtext += chr ((ord(char)  + number - 65) % 26 + 65) 
		elif (char.islower()):
			encryptedtext += chr((ord(char)+ number- 97) % 26 + 97)
		else :
			encryptedtext += char

	return encryptedtext

def ceaser_CryptograpyDecrypted(message, number):
	if(number < 0 and number >26):
		ceaser_CryptographyDecrypted()
	
	decryptedtext = ' '
	for char in message:
		if(char.isupper()):
			decryptedtext += chr ((ord(char)  - number - 65) % 26 + 65) 
		elif (char.islower()):
			decryptedtext += chr((ord(char)- number- 97) % 26 + 97)
		else :
			decryptedtext += char

	return decryptedtext
	


message = input("Enter a text message: ")
number = int(input("Enter a number between 0 and 26 : "))

encrypted = ceaser_CryptographyEncrypted(message, number)
decrypted = ceaser_CryptograpyDecrypted(encrypted, number)

print("The coded message is :", encrypted)
print("The decoded message is :", decrypted)