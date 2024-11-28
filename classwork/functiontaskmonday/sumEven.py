def sumEven_num(numbers):
	total = 0
	return[numberfor number in numbers
		if number % 2 == 0]

print(sumEven_num([2,7,9,17,19,2,8,10]))