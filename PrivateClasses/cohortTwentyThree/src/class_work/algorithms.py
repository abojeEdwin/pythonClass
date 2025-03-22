def is_anagram(s1,s2):
    return set(s1) == set(s2)
print(is_anagram("elvis","lives"))

def is_contains(nums,x):
    return x in nums
print(is_contains([3,3,4,5,6,111,5],111))

def find_duplicates(nums):
    duplicates ,seen = set(), set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)
print(find_duplicates([3,3,4,5,6,6,111,5]))

lst = list(range(10)) + list(range(10)) #Remove all duplicate from a list
lst = list(set(lst))
print(lst)

def find_pairs(nums,x):
    pairs = []
    for (i,num ) in enumerate(nums):
        for (j,num2) in enumerate(nums[i+1:]):
            if num + num2 == x:
                pairs.append([num,num2])
    return pairs

print(find_pairs([3,4,5,6,111],10))

def is_palindrome(phrase):
    return phrase == phrase[::-1]
print(is_palindrome("anna"))

i = [3,4]
i+=[5,6]
print(i)
i.append(10)
print(i)
i.pop()
print(i)
i.insert(0,10)
i.pop()
print(i)


def get_missing_number(ist):
    return set(range(ist[len(ist)-1])[1:]) - set(i)
i = list(range(1,10))
i.remove(5)
print(get_missing_number(i))


def intersection(lst1, lst2):
    res , ist2_copy = [] , lst2[:]
    for x in lst1:
        if x in ist2_copy:
            res.append(x)
            ist2_copy.remove(x)
    return res

i = [80,2,99,888,-300]
largest = max(i)
smallest = min(i)
print(largest,smallest)


def reverse(string):
    if len(string) <= 3 : return string
    return reverse(string[1:]) + string[0]
print(reverse("moodboard"))