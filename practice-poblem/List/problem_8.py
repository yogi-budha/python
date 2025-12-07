list1 = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

# def addList():
#     list2 = []
#     for i in list1:
#         temp = ""
#         for j in i:
#              temp = temp + j
#         list2.append(temp)
#     print(" ".join(list2))
    

# addList()


# using the list comprehension

result = ["".join(i) for i in list1]

print(" ".join(result))
