#  Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Exercise 1:

# Input:

# [1,2,3,3,3,3,4,5]
# Output:

# [1, 2, 3, 4, 5]

def UniqueList(s):
    x = []
    for i in s:
        if i not in x:
            x.append(i)
    return x

result = UniqueList([1,2,3,4,5,5,4,3,2,1,1])
print(result)