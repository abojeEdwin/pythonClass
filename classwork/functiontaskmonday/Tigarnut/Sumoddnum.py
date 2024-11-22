def get_odd_sum(numbers):
	sum = 0
	for number in numbers:
		if number % 2 != 0:
			sum+=number
	return sum





print(get_odd_sum([1,2,3,4,5]))
			