test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]

test_dist = []

for i in range(0,len(test_list),len(key_list)):
    temp = test_list[i:i+len(key_list)]
    result = {k:v for k,v in zip(key_list,temp)}
    test_dist.append(result)

print(test_dist)