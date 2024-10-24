Positive_input = 0
Zero_input = 0
Negetive_input = 0

number1 = int(input("Enter the first number :"))
number2 = int(input("Enter the second number :"))
number3 = int(input("Enter the third number :"))
number4 = int(input("Enter the fouth number :"))
number5 = int(input("Enter the fifth number :"))

if number1 > 0:
	Positive_input += 1
elif number1 < 0:
	Negetive_input += 1
if number1 == 0:
	Zero_input += 1

if number2 > 0:
	Positive_input += 1
elif number2 < 0:
	Negetive_input += 1
if number2 == 0:
	Zero_input += 1

if number3 > 0:
	Positive_input += 1
elif number3 < 0:
	Negetive_input += 1
if number3 == 0:
	Zero_input += 1

if number4 > 0:
	Positive_input += 1
elif number4 < 0:
	Negetive_input += 1
if number4 == 0:
	Zero_input += 1

if number5 > 0:
	Positive_input += 1
elif number5 < 0:
	Negetive_input += 1
if number5 == 0:
	Zero_input += 1

print("Number of Negetive input equals :", Negetive_input)
print("Number of Positive inputs equals :", Positive_input)
print("Number of Zero inputs equals :", Zero_input)