#  Write a Python program to add three given lists using Python map and lambda.
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [11,12,13,14,15]

result = list(map(lambda x,y,z:x+y+z,list1,list2,list3))

print(result)