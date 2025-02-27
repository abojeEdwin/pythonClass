def find_middle(word,ce):
    new_word = " "
    wordcount= len(word)
    if wordcount % 2 == 0:
        new_word = word[:wordcount//2] + ce + word[wordcount//2:]
    else:
        new_word = word + ce
    return new_word


print(find_middle("heloo","ce"))




