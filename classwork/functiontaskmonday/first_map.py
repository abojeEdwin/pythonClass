def even_num(number:list):
	return[num for num in numbers if num % 2 == 0]


numbers = [10,3,7,1,9,4,2,8,5,6]
list(filter(even_num,numbers))
print(even_num(numbers))