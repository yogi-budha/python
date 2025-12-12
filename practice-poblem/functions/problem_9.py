
#  Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def evenNumber(list1):
    newList = []
    for i in list1:
        if i%2 ==0:
            newList.append(i)
    return newList

evenList = evenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(evenList)