def uzo(number):
	return[num for num in range(1,number+1)]
	

def cube_root(uzo):
	cube=[]
	for num in uzo:
		cube.append(num**3)

	return cube



print(cube_root(uzo(5)))
