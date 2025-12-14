# Use reduce to convert a 2D list to 1D
import functools
list1 = [[1,2,3],[4,5,3,4,5],[6]]


result = functools.reduce(lambda x,y:x+y,list1)

print(result)