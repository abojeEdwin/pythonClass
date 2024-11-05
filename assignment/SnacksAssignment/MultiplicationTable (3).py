column_start = 2
column_end = 24
row_start = 2
row_end = 20

for i in range(column_start, column_end + 1):
	print(f"{i}: ", end="")
	for j in range(row_start, row_end + 1):
	print(j, end="")
print( )