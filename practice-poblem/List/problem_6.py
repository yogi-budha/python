list1 = ['1ac21', '23fg', '456', '098d','1','kls']
def number(s):
    list2 = []
    product=1
    for i in s:
        if i.isdigit():
            list2.append(i)
        
    for i in list2:
        product *=int(i)

    return product

a = sorted(list1,key = number , reverse=True)

print(a)