# Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

# Example 1:

# Input:

A = "apple banana mango" 
B = "banana fruits mango"

Asp = A.split()
Bsp = B.split()

concatval = Asp + Bsp
result = []
for i in concatval:
    if concatval.count(i)==1:
        result.append(i)

print(result)