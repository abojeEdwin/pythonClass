def get_average_func(numbers):
	average = 0
	total = 0
	for number in numbers:
		total+=number
		average = total / len(numbers)

	return average




print(get_average_func([10,20,30,40]))	