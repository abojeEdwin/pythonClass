
def get_sum_func(numbers):
	total=0
	for number in numbers:
		if number % 2 == 0:
			total+=number
	return total








print(get_sum_func([1,2,3,4]))

