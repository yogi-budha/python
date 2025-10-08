# Print the following pattern. Write a program to use for loop to print the following reverse number

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# solution 

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

##################################################################################################################

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# solution

for i in range(1,10):
    if(i<6):
        for j in range(i):
            print("*",end=" ")
    else:
        for k in range(10-i,0,-1):
            print("*",end=" ")
    print()



###################################################################################################################

#     *
#   * * *
# * * * * *


# solution

for i in range(1,4):
    for j in range(3-i):
        print(" ",end=" ")
    for k in range((i*2)-1):
         print("*",end=" ")
    print()


###########################################################################################################################

# 1

# 2 1

# 3 2 1

# 4 3 2 1

# 5 4 3 2 1

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    print()

###############################################################################################################################



