# find the given number is prime or not

num = int(input("Enter any number"))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("The number is not prime number")
        else:
            print("The number is a prime number")