list1 = ['campusxIs', 'bestFor', 'dataScientist']
list2 = []
for i in list1:
    temp = ""
    for j in i:
        if(j.isupper()):
            temp = temp +" "
        temp = temp + j
    list2.append(temp)

print(" ".join(list2))