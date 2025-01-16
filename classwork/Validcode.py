validator = 1
largest = 0
while validator >= 0:
	score=int(input("Enter number"))
	if score > largest:
		largest = score
		validator = validator + 1
		validator += 1
	else:
		print("invalid input")
		validator = 1
		print("largest is", largest)
	
		