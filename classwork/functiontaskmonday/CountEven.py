def count_even(number):
	return len([count for count in number if count % 2 == 0])

print(count_even([1,5,7,3,2,9,8,10]))
