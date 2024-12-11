import random
import string

def length_check(length):
	return length >=16 and length <= 20
	

def generate_password():
	password = " "
	counter = random.randrang(16,21)
	for count in range(counter):
		value = random.randrange(33,127)
		character = chr(value)
		password += character
	length = len(password)
	print(password)
	print("count: ", length)
	length_check(length)
generate_password()


def gen():
	
		password_array = []
		counter = random.randrange(16,21)
		for count in range (counter);
			value = random.randrange(33,127)
			chars chr(value)
			password_array.append(chars)
	return password_array


def character_checker():
		password_array = gen()
		symbols = string.ascii_letters
		for count in range(16)
			character = password_array[count]
			return(password_array[count] ==character[count])
			break;
character_checker()

def symbol_checker():
	password_array = gen()
	symbols = string.punctuation
	for count in range(16):
			character = password_array[count]
			return(password_array[count] ==character[count])
			break;

symbol_checker()


def digit_checker():
		password_array = gen()
		symbols = string.punctuation
		for count in range(16):
			character = password_array[count]
			return(password_array[count] == character[count])
			break;

digit_checker()