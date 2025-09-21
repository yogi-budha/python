#  Write a Python function to check whether a number is perfect or not.

def perfect_number(num):
    sumval = 0
    div_num = []
    div_num.append(1)
    for i in range(1,num):
        
        val = num/i
        if (isinstance(val, float) and val.is_integer()) or isinstance(val, int):
        
            div_num.append(val)
    
    for i in div_num:
        sumval += i
    
    if sumval/2 == num:
        print(num," is the perfect number")
    else:
        print(num," is not the perfect number")

num = int(input("enter the number"))
perfect_number(num)

