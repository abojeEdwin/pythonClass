import math
n = int(input("Enter number of sides on the polygon :"))
s = int(input("Enter the length of one of th sides :"))
pi = 3.142
Area_of_a_polygon = (n * pow(s,2)) / (4*math.radians(pi / n))
print(Area_of_a_polygon)