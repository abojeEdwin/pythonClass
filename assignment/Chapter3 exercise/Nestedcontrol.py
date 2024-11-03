Largestnumber = None
Secondlargest = None

for i in range (10):
	number = int(input("Enter the number :"))

if Largestnumber is None or number > Largestnumber:
	Largestnumber = number
if Secondlargest is None or nuumber < Largestnumber:
	Secondlargest = number 

print(Largestnumber)
print(Secondlargest)