def mixed_case(words):
    mixed_case_words = ''
    lower_case_words = ''
    for cha in words:
        if cha.isupper():
            mixed_case_words += cha
        if cha.islower():
            lower_case_words += cha

    return mixed_case_words+lower_case_words
