def get_prime_Num(number):
	primenum = []
	if(number == 9):	
		return number

	if(number == 2):
		return number

	for num in range (1,number):
		if(num % number == 0):
			primenum.append(primenum)

	return num



print(get_prime_Num(20))





	
		