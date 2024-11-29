def square_num(number):
	if type(number) is int: return[num * num for num in range(1,number)]

	raise TypeError






print(square_num(16))