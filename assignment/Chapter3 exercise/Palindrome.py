number = int(input("Enter a five digit number :"))
firstnumber = number // 10000
secondnumber = number // 1000 % 10
thirdnumber = number // 100 % 10
reversednumber = number // 10 % 10
fifthnumber = number % 10

if (firstnumber == fifthnumber and secondnumber == reversednumber):
	print("its a palindrome")
else :
	print("its not a palindrome")
