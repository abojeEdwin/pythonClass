def get_arb_product(*args):
	product = 1
	for digits in args:
		product *= digits

	return product



print(get_arb_product(2,5,6))
	