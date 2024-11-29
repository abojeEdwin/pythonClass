def get_only_num(words):
	return[int(num)for num in words if num.isdigit()]
	


print(get_only_num('abc123de456'))