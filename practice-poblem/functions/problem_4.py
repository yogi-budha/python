# Use reduce to convert a 2D list to 1D
import functiontools

list1 = [1,2,3,4,5,6]

temp = functiontools.reduce(lamdba x,y: x+y,list1)
print(temp)