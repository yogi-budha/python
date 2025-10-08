# Display Fibonacci series up to 10 terms.

a=0
b=1
sumval = 0
for i in range(0,10):
    print(a)
    sumval = a+b
    a=b
    b=sumval