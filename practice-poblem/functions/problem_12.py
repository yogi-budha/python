

def countString(s):
    currentCountval = 0
    maxCountval = 0
    currentWord = None
    maxCurrentWord = None
    splitString = s.split(" ")
    for i in splitString:
        currentCountval =splitString.count(i)
        currentWord = i
        if(currentCountval>maxCountval):
            maxCountval = currentCountval
            maxCurrentWord = currentWord
    print(maxCurrentWord,maxCountval)

countString("hello how are you i am fine fine fine thank you")

