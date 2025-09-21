# import random

# randomNumber = random.randint(1,50)
# i = 1
# while i<10:
#     number = int(input("Guss the number:"))
#     if number == randomNumber:
#         print("Jackpot you gussed it right at ",i," try.")
#         break
#     elif number > randomNumber:
#         print("The number must be less then ", number)
#     else:
#         print("The number greater then ", number)
#     i +=1

# else:
#     print("you cannot guss the right the correct number")

# t = 10000

# for i in range(10,0,-1):
#     print("The ",i,"year population is",t)
#     t = t/1.1


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for k in range(i-1,0,-1):
#         print(k,end=" ")
#     print()



# string = input(" Enter the any string:  " )
# term = input("Enter the term you want to remove: ")

# stringlist = string.split("@")

# print(stringlist[0])

# for i in string:
#     if(i == "@"):
#         break
#     else:
#         print(i,end="")

# index_of_at = string.find("@")
# username = string[:index_of_at]
# print(username)

# count = 0   

# for i in string:
#     if(term == i):
#         continue
#     else:
#         print(i,end="")


# find the given string is palindrome or not

# string = input("Enter the string:")

# reverse_string = string[::-1]

# if(string == reverse_string):
#     print("The given string is palindrome")
# else:
#     print("The given string is not palindrome")

# flag = True

# for i in range(len(string)//2):
#     if string[i] !=string[len(string)-i-1]:
#         flag = False
#         print("The given string is not palindrome number")
#         break

# if flag:
#     print("The given string is palindrome number")


# count =0

# split_string = []

# for i in string:
#     if i != " ":
        

# print(count)

# str = []

# temp = ''

# for i in string:
#     if i != " ":
#         temp = temp + i
#     else:
#         str.append(temp)
#         temp=" "
# str.append(temp)

# print(str)

# s = []
# for j in string.split(" "):
#     s.append(j[0].upper()+j[1:].lower())

# print(" ".join(s))



# conver integer into string

number = int(input("Enter the number"))

digits = '0123456789'
result = ''
while number != 0:
    result = digits[number%10] + result
    number = number//10

print(result)
print(type(result))
