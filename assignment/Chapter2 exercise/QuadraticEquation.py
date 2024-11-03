import math
a = int(input("Enter the value of a :"))
b = int(input(" Enter the value of b :"))
c = int(input(" Enter the value of c : "))

x = -b + (math.sqrt(b * b * 4 * a * c))
y = -b- (math.sqrt( b + b * 4 * a *c))

root1 = x / 2 * a
root2 = y / 2 * a
print("The roots are" , root1, "and", root2)