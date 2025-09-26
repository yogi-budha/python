# Find the maximum unique element

test_dict = {
    "y":[1,2,3,4,5,6],
    "o":[1,2,3,2,1,2],
    "g":[1,6,7,89,6,2],
    "e":[1,2,3,4,2,1]
}
max_key = None
max_unique_value_length = -1

for (key,value) in test_dict.items():
    temp = set(value)
    unique_value_length = len(temp)
    if(unique_value_length > max_unique_value_length):
        max_unique_value_length = unique_value_length
        max_key = key 

print(max_unique_value_length,max_key)