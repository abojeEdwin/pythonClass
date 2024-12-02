import localDate

weekNum = int(input("Enter today's day (0 - 6): "))
daysElapsed = int(input("Enter the nunber of days elapsed since today"))
match(weekNum):
		case 0:
			print("Sunday")
		case 1:
			print("Monday")
		case 2:
			print("Tuesday")
		case 3:
			print("Wednesday")
		case 4:
			print("Thursday")
		case 5:
			print("Friday")
		case 6:
			print("Saturday")


if weekNum != 0-6:
	print("Invalid input, please try again")

		