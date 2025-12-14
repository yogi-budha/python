

# Write a Python function to check whether a number is perfect or not.
# A Perfect number is a number that is half the sum of all of its positive divisors (including itself).

# Example :

# The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
# import math
# num1 = int(input("Enter the number:"))
# list1 = [num1]
# num = num1
# while(num>1):
#     if(num%2) == 0:
#         num = num/2
#     else:
#         num = math.ceil(num/2)
#     list1.append(num)
    
# print(list1)

# sum = 0
# for i in list1:
#     sum += i

# result = int(sum//2)
# print(result,num1)

# if(result == num1):
#     print(result)
    
#     print("the number is the perfect number")
# else:
#     print("the number is not the perfect number")


num = int(input("Enter the number: "))

divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        print(i)
        divisor_sum += i

if divisor_sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

