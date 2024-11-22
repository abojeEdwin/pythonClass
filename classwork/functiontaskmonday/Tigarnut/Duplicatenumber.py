def get_duplicate_num(numbers):
	for count in numbers:
		for counter in numbers:
			if numbers[count] == numbers[counter]:
				return True
		else:
			return False




print(get_duplicate_num([1,2,3,4,5,2]))