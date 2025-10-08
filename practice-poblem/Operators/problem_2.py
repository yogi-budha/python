# Write a menu-driven program -
# 1. cm to ft
# 2. km to miles
# 3. USD to INR
# 4. exit

inputval = int(input("""
1. cm to ft
2. km to miles
3. USD to NPR
4.exist 

"""))


if(inputval == 1):
    cmval = int(input("enter the centemeter: "))
    res = 0.0328084 * cmval
    convertedMessage = "The {0} cm converted into {1} feet".format(cmval,res)
    print(convertedMessage)
elif inputval == 2:
    kmvall = int(input("enter the kilometer: "))
    miles = 0.62137119 * kmvall
    convertedMessage = "The {0} kilometer converted into {1} miles".format(kmvall,miles)
    print(convertedMessage)
elif inputval == 3:
    usdCurr = int(input("enter the usd currency: "))
    npr = 141.95 * usdCurr
    convertedMessage = "The {0} usd converted into {1} nepali ruppese".format(usdCurr,npr)
    print(convertedMessage)
else:
    exist()