def get_acronyms_func(word):
	letter = word.split()
	acronyms = ''.join(word[0].upper() for word in letter)

	return acronyms






print(get_acronyms_func("Portable Network Graphics"))