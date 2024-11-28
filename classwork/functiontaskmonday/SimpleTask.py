def get_even_sum(numbers):
	return([False if num % 2 != 0 else True for num in numbers])



print(get_even_sum([10,3,7,1,9,4,2,8,5,6]))
