def ispalindrome_List(words):
	return[word == word[::-1] for word in words]




print(ispalindrome_List(['madam','apple','racecar','']))