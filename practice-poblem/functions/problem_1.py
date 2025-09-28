# Write a Python program to print the even numbers from a given list.

list1 = [1,2,3,4,56,7,2,1,3,3,2,88,20,8]

# def print_even(list1):
#     newList = []
#     for i in list1:
#         if i%2 == 0:
#             newList.append(i)
#     print(newList)

# print_even(list1)

evenval = list(map(lambda x :x%2 == 0,list1))
print(evenval)