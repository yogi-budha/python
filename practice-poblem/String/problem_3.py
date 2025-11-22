x = float(input("enter the number:"))
term = int(input("enter the term:"))
sum = 0 

for i in range(1,term+1):
    if( i == 1):
        sum = sum + (x-1)/2
    else:
        sum = sum + 0.5 * ((x-1)/x)**i
print("the sum of the series is:", sum)