def sum_num(numbers):
	total = 0
	for num in numbers:
		total+=num

	return total


def sum_even_numbers(numbers):
	return sum_num([num for num in numbers if num % 2 == 0])

print(sum_even_numbers([1,2,3,4,5,7,8,9,10,12,15,20,100]))