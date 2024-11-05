number_of_passed = 0
number_of_failed = 0

for i in range(1,15):
	score = int(input("Enter score :"))
	if (score >= 45):
		number_of_passed +=1
	else:
		number_of_failed +=1
print("The number of passed is :",number_of_passed,"\n","The number of failed is:",number_of_failed)

	