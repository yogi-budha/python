#  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47

def countUpperLower(string):
    countUpper = 0
    countLower = 0
    for i in string:
        if i.isupper():
            countUpper +=1
        elif i.islower():
            countLower +=1
    print("No. of upper case characters: ", countUpper)
    print("No. of lower case characters: ", countLower)


countUpperLower('CampusX is an Online Mentorship Program fOr EnginEering studentS.')