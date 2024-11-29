def number_of_list(words,number):
	return [word for word in words if len(word)>= number]

print(number_of_list(["Apple","Fish","Orange","Ice","Lime","Hippopotemus","Earth"],5))