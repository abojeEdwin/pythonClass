def first_task(word):
    new_dict = {}
    for char in word:
        key = new_dict[char]
        for char2 in new_dict:
            if char in new_dict:
                char+=1
            else:
                char = 1
    return new_dict

print(first_task("semicolon.africa"))



