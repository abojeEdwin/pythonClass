def funcCheckElement(number,elementToSearch):

	if (elementToSearch in number):
		return("Element occurs in the list")
	else: return("Element does not occur in the list")

	



number = [20,39,50,90,10]
elementToSearch = 87

print(funcCheckElement(number,elementToSearch))
