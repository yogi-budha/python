# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# Input:

list1 = [1,2,3,4,5,6]
# Output:

# [1,3,6,10,15,21]

sum = 0
result = []

for i in list1:
    sum += i
    result.append(sum)
print(result)