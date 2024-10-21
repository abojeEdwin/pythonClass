m =  'monthly payment value'
p =  'principal'
r =  'rate'
n = 'duration of the loan'

p = int(input("Enter the principal :"))
r = int(input("Enter the annual interest rate :"))
n = int(input("Enter the duration in years :"))

Monthly_Percent_Rate = r / 100 / 12
Monthly_Duration = n * 12
m = p * ( Monthly_Percent_Rate *( 1 + Monthly_Percent_Rate ) **Monthly_Duration) / (( 1 + Monthly_Percent_Rate)**Monthly_Duration -1)

print(f'Your monthly payment is ${m}')