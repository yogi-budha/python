# Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

num = int(input("enter any number: "))

sum = 1

for i in range(2,num+1):
    term = num**i/i
    sum = sum + term
    print(sum)
print("total sum is :",sum)