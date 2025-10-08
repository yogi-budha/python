#  Find the factorial of a given number.

factNum = int(input("Enter the number: "))
factval = 1
for i in range(1,factNum+1):
    factval *= i
print(factval)