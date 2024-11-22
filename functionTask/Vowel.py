
def my_vowel(word):

	vowels="aeiouAEIOU"
	count = 0

	for character in word:
		if character in vowels:
			count += 1

	
	return count
	


user_input = input("Enter a string:")


print (my_vowel(user_input)) 
