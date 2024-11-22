def skip_sum(number):
	total = 0
	for i in number:
		for j in number:
			total+=j
		total = total - i
			
	return total




print(skip_sum([1,2,3,4,5]))		
		
		
		
