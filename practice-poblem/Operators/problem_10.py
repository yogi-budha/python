#  Write a program that can remove all the duplicate characters from a string. User will provide the input.

str = input("Enter any things: ")

for i in str:
    if i not in str:
        print(i,end="")