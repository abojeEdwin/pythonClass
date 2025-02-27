def return_occurance(word,target):
    count = 0
    for char in word:
        count += char.count(target)
    return  target,count
