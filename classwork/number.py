number = int(input ("Enter the three digits :"))
firstnum = number // 100
secondnum = number % 10
thirdnum = number // 10
fourthnum = thirdnum % 10
print(secondnum,fourthnum,firstnum)
even = 0
odd = 0
if secondnum % 2 == 0:
      even=even +1
else:
	odd = odd +1
if  firstnum % 2 == 0:
        even = even +1
else:
        odd = odd +1
if fourthnum % 2 == 0:
        even = even +1
else:
        odd = odd + 1


print("number of even numbers are" ,even)
print("number of odd numbers are" ,odd) 