
inputval = int(input("Enter no. of record: "))
records = []
jobRequirementsDetails = ("engineering","python","2022")

for i in range(1,inputval+1):
    print("Enter the details of student",i)
    name = input("Enter student name: ")
    hignerEducation = input("Enter Higher Education: ")
    primarySkill = input("Enter primary skill: ")
    yearOfGraduation = input("Enter year of graduation: ")
    records.append((name,hignerEducation,primarySkill,yearOfGraduation))

for i in records:
    if i[1] == jobRequirementsDetails[0] and i[2]== jobRequirementsDetails[1] and i[3]== jobRequirementsDetails[2]:
        print("Congratulation",i[0],"you are selected for the job")
    else:
        print("Sorry",i[0],"you are not selected for the job")
