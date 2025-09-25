# A dictionary contains following information about 5 employees:

# First name
# Last name
# Age
# Grade(Skilled,Semi-skilled,Highly skilled)
# Write a program using map/filter/reduce to a list of employees(first name + last name) who are highly skilled



employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }

]

highlymember = list(filter(lambda x:x["grade"] == "skilled" ,employees))

for member in highlymember:
    print(member["fname"],member["lname"])
# print(highlymember)