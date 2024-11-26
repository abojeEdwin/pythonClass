def isPrime(number : int)-> bool:
	if(number == 2):
		return True

	if(number % 2 == 0):
		return False
	
	for count in range(3,2):
		count * count <= number
		if(number % count == 0):
			return False
	


	return True
		
	






print(isPrime(10))	