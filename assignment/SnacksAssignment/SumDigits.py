number = int(input("Enter a number between 0 and 1000 :"))

FirstRemainder = number % 10
Center = number / 10
thirdnum = number % 10
fourthnum = Center / 10

SumDigit = FirstRemainder + thirdnum + fourthnum

print("The sum digit is :", SumDigit)