firstnumber = int(input("Enter first number : "))
secondnumber = int(input("Enter second number : "))
thirdnumber = int(input("Enter third number : "))

smallest = firstnumber
middlenumber= secondnumber
largestnumber = thirdnumber

if(smallest < secondnumber):
	secondnumber = smallest
if(smallest < thirdnumber):
	thirdnumber = smallest 
if(middlenumber < secondnumber):
	secondnumber = middlenumber
if(middlenumber < thirdnumber):
	thirdnumber = middlenumber
if(largestnumber > secondnumber):
	secondnumber = largestnumber
if(largestnumber > thirdnumber):
	thirdnumber = largestnumber

print(smallest ,  middlenumber , largestnumber)