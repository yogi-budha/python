# Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,2,9,64,625,-]

result = list(map(lambda x:x[1]**x[0],enumerate([1,2,3,4,5])))

print(result)