# Using filter() and list() functions and .lower() method filter all the vowels in a given string.

string = "CampusX is an Online Mentorship Program fOr EnginEering studentS."

result = list(filter(lambda x:x.lower() in ['a','e','i','o','u'],string))

print(result)