num1 = int(input("Enter the first integer :"))
num2 = int(input("Enter the second integer :"))
num3 = int(input("Enter the third integer :"))
  
if num1 <= num2 <= num3:
    smallest = num1 
    largest = num3
else:
    middle = num2
if num2 <= num1 <= num3:
    smallest = num2
    largest = num3
else:
    middle = num1
if num3 <= num1 <= num2:
    smallest = num3
    largest = num2
else:
    middle = num1
if num3 <= num2 <= num1:
    smallest = num3
    largest = num1
else:
    middle = num2

print("""""""",smallest,middle,largest)