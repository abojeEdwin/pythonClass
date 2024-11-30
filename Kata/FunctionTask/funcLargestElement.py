def funcLargestElement(numbers):
	largest = numbers[0]
	for index in numbers:
		if(index > largest):
			largest = index
	
	return largest
		
	
	




numbers = [15,25,60,1,76]
print(funcLargestElement(numbers))