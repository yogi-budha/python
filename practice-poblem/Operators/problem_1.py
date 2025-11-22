# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

# a = int(input("Enter the 1st angle: "))
# b = int(input("Enter the 2nd angle: "))
# c = int(input("Enter the 3rd angle: "))

# sum = a+b+c

# if(sum == 180):
#     print("It form a triangle")
# else:
#     print("It doesnot form a triangle")


# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

if(sp<=cp):
    print("loss")
else:
    print("profit")