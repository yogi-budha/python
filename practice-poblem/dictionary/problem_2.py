test_str = 'CampuX best for DS student'
rep_dict = {
    "best":"is the best",
    "DS" : "Data-science"
}

newStr = []

for i in test_str.split(" "):
   if i in rep_dict:
    newStr.append(rep_dict[i])
   else:
    newStr.append(i)

print(newStr)

new_test_str = " ".join(newStr)
print(new_test_str)
