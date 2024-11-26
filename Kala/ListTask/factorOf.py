def factorOf(number : int) -> int:
	
	if(number <= 0):
		return 0

	numberoffactors = 0
	for count in range(1,int(number**0.5)+1):
		if(number % count == 0):
			numberoffactors+=1
		if(number != count // count):
			numberoffactors+=1

	return numberoffactors



print(factorOf(10))