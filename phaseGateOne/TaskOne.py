import random

a = random.randrange(10)
b = random.randrange(10)

sum = a+b

userInput = int(input("Enter the sum of both integers : "))
if(userInput == sum):
	print(True)
else:
	print(False)


