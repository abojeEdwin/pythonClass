def getSwitchList(numbers:list,number:int):
		for _ in range(number):
			each = numbers[0]
			numbers.remove(numbers[0])
			numbers.append(each)

		return numbers








numbers = [1,2,3,4,5]
number = 2
print(getSwitchList(numbers,number))