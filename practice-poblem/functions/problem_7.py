
def sortedString(s):
    string = s.split("-")
    return "-".join(sorted(string))

string = "green-red-yellow-black-white"

print(sortedString(string))