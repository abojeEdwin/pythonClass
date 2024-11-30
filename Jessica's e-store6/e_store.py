cart=[]
total=[]
product= []
userInput = 0


def add_to_cart():
	product = input("Enter product name or press 0 to exit:")
	if product.casefold() == 'laptop':
		cart.append("laptop-$1000")
		total.append(1000)
		print("You have added Laptop - $1000 to cart")
	elif product.casefold() == 'phone':
		cart.append("phone - $500")
		total.append(500)
		print("You have added phone - $500 to cart")
	elif product.casefold() == 'headphones':
		cart.append("headphones - $100")
		total.append(100)
		print("You have added headphones- $100 to cart")
	elif product == '0':
		exit()
	else:
		print("Invalid input, please try again")
		add_to_cart()

def remove_from_cart():
	product = input("Enter the product name you will like to remove or press 0 to exit:")
	if product.casefold() == 'laptop':
		cart.remove("laptop-$1000")
		total.remove(1000)
		print("Laptop has been removed from your cart laptop=$1000")
	elif product.casefold() == 'phone':
		cart.remove("phone-$500")
		total.remove(500)
		print("Phone has been removed from your cart phone-$500")
	elif product.casefold() == 'headphone':
		cart.remove("headphones-$100")
		total.remove(100)
		print("Headphones has been removed from your cart Headphones-$100")
	elif product == 0:
		exit()
	else :
		print("Invalid input,please try again ")
		add_to_cart()

def check_out():
	totalcheckout = 0
	for item in total:
		totalcheckout+=item
	print(f"Here's an invoice of your purchase {cart} total is ${totalcheckout}")
	exit()

def view_cart():

	return print(cart)

def view_product():
	return "1. Laptop-$1000\n2. phone-$500\n3. headphones-100"

def exit():
	return menu()

def menu():

	JessicaUserInput = int(input("Welcome to Jessica's e-store.\nPlease Enter A Valid Option\n1. View Products\n2. Add Item Cart\n3. View Cart\n4. Remove Item From Cart\n5. CheckOut\n6. Exit \nEnter an option  "))
	if JessicaUserInput == 1:
		print (view_product())
	elif JessicaUserInput ==  2:
		(add_to_cart())
	elif JessicaUserInput == 3:
		 (view_cart())
	elif JessicaUserInput == 4:
		(remove_from_cart())
	elif JessicaUserInput == 5:
		 (check_out())
	elif JessicaUserInput  == 6:
		return print("Exiting")
		

while(userInput != 6):
		view_product()
		menu()
						
			






print(menu())
print(view_product())
print(add_to_cart())
print(view_cart())
print(remove_from_cart())
print(checkout())
	
	