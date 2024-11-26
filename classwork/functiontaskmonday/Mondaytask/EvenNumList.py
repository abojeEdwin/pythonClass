def getNumList(numbers):
	listnum = []
	for count in numbers:
		if(count % 2 == 0):
			listnum.append(True)
		else:
			 listnum.append(False)
	return listnum






input = [1,2,3,4,5]
print(getNumList(input))	