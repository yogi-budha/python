# Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.

# take user input
N = int(input("Enter a number: "))

i = 1
total = 0

while i <= N:
    if i % 5 == 0:   # skip numbers divisible by 5
        i += 1
        continue
    
    total += i
    
    if total > 300:  # stop if sum exceeds 300
        break
    
    i += 1

print("Final Sum:", total)

