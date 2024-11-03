number = int(input("Enter the five digit number:"))
firstdigit = number // 10000
secondigit = (number // 1000 % 10)
thirdigit = (number // 100 % 10)
fourthdigit = (number // 10 % 10)
fifthdigit = (number %10)
print(firstdigit,   secondigit,   thirdigit,   fourthdigit,   fifthdigit)