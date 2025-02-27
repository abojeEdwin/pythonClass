def first_task(word):
    new_dict = {}
    for char in word:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return new_dict





