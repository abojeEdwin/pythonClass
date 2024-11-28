def get_even_sum(numbers):
	return sum([num for num in numbers
		if num % 2 != 0])

print(get_even_sum([5,9,91,54,29,6]))