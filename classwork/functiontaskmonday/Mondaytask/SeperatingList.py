def SeperatingList(numbers):
	firsthalf = []
	secondhalf = []
	avernum = []
	avernum = len(numbers)/2
	for count in avernum:
		if(count > len(avernum)):
			firsthalf = count
		if(count < len(avernum)):
			secondhalf = count

	return num



number1 = [1,2,3,4,5]
print(SeperatingList(number1))