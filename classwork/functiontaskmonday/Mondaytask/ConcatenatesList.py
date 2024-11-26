def ConcatenateList(numbers):
	avernum = len(numbers)/2
	num = numbers.slice(0::avernum)


	return num



number1 = [1,2,3,4,5]
print(ConcatenateList(number1))