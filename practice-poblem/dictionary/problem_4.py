# : Key with maximum unique values
# Given a dictionary with values list, extract key whose value has most unique values.

# Example 1:

# Input:

# test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# Output:

# CampusX
# Example 2:

# Input:

test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output:

# Best

ans = None,
count = 0
for key,value in test_dict.items():
    arr = []
    for i in value:
        if(i not in arr):
            arr.append(i)
    if(len(arr)>count):
        count = len(arr)
        ans = key

print(ans)