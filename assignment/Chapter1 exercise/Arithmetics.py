integer1 = int(input("Enter the first integer :"))
integer2 = int(input("Enter the second integer :"))
integer3 = int(input("Enter the third integer :"))

sumation = integer1 + integer2 +integer3
average = integer1 + integer2 +integer3 / 3
product = integer1 * integer2 *integer3

print("The sum of the integers is",sumation)
print("The average is",average)
print("The product is",product)

largest = integer1
smallest = integer1

if integer2 > largest:
	largest = integer2
else:
	integer3 > integer2
	largest = integer3
if integer2 < smallest:
	smallest = integer2
else: 
	integer3< integer2
	smallest = integer3
	
print("The largest integer is",largest)
print("The smallest integer is",smallest)