#  Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

sum = 0

n = int(input("enter the number"))
count = 1
while n !=0:
    sum += n
    n = int(input("enter the number"))
    count +=1
else:
    print("the sum is: ",sum)
    avg = sum / count
    print("the avg is: ", avg)

    

  
    

