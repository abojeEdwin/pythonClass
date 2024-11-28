def prime_num(number):
	allprimenumbers=[]

	for num in number:
		count = 0
		for index in range(1,num):
			if num % index == 0:
				count+=1

		if  count == 1:
			allprimenumbers.append(num)



	return allprimenumbers





print(prime_num([5,9,7,10,11,3,2,12]))




		
	