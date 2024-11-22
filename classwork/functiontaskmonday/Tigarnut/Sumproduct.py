def get_sum_product(num):
	total = 0

	num_of_element_in_list = len(num)

	for i in range(num_of_element_in_list):

		for j in range(i,num_of_element_in_list):

			total += num [j] * num [i]

	return total

num = [1,2,3,4]

print(get_sum_product(num))