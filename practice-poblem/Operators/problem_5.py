#  Reverse a given integer number.

number = int(input("Enter the any number: "))
while number!=0:
    a = number%10
    number= number//10
    print(a,end="")
