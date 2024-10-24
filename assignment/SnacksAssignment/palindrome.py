number = int(input("Enter the number :"))

original_number = number
reversed_num = 0
remainder = 0


while (number > 0):
	remainder = number % 10
	reversed_num = reversed_num * 10 + remainder
	number = number // 10

if original_number == reversed_num:
	print("it is a palindrome")

else:

	print("It is not a palindrome ")