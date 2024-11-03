print(f' {"number":>6} {"square":>6} {"cube":>6}')
for i in range (6):
	square = i ** 2
	cube = i **3
print(f'{i:<6} {square:<6} {cube:<6}')