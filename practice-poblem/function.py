# color_name="green-red-yellow-black-white"

# def sortedName(color_name):
#     list_colorName = color_name.split("-")
#     sorted_color_name_list = sorted(list_colorName)
#     sorted_color_name = "-".join(sorted_color_name_list)
#     return sorted_color_name
    

# print(sortedName(color_name))

string_val =  'HI tehere.'

def countAlp(string_val):
    capitalLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smallLetter = 'abcdefghijklmnopqrstwxyz'
    countUpperCaseLetter = 0;
    countSmallCaseLetter = 0;
    for i in string_val:
        for j in capitalLetter:
            if i == j:
                countUpperCaseLetter = countUpperCaseLetter + 1
        for k in smallLetter:
            if i == k:
                countSmallCaseLetter = countSmallCaseLetter+ 1

    return (countUpperCaseLetter,countSmallCaseLetter)

print(countAlp(string_val))