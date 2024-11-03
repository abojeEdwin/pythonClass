age = int(input("Enter your age :"))

maximumheartrate_bpm = 220  - age
print("Your maximum heart rate is :",maximumheartrate_bpm)

#Target heart rate is 50% - 85%#

targetheartrate_low = maximumheartrate_bpm *50 / 100
targetheartrate_high = maximumheartrate_bpm *85 / 100

print("Your low target heart rate is:",targetheartrate_low)
print("Your high target heart rate is:",targetheartrate_high)


