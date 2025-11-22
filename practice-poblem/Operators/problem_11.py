# Find a location of a word in a given sentence.

sentence = "We can learn data science through campusx mentorship program"
word = "campusx"
inArr = sentence.split()
for i in range(0,len(inArr)):
  if(inArr[i] == word):
    print("Location of the word is",i+1)