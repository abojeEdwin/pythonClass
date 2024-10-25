one_pound = 2.20462
one_inch = 39.37
height = float(input("Enter your weight in pounds :"))
weight = float(input(" Enter your height in inches :")) 

height_met = height / one_inch
weight_kg = weight / one_pound

Body_Mass_Index =  weight_kg / height_met * height_met
print("BMI is: " ,+ Body_Mass_Index)