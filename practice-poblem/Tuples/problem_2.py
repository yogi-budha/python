arr = (1,5,7,8,10)
result = 0
arr2 =[]

for i in range(len(arr)):
    if arr[i]==0:
        result = arr[i] * arr[i+1]
    elif arr[i] == arr[-1]:
        result = arr[i] * arr[i-1]
    else:
        result = arr[i] * arr[i-1]  + arr[i] * arr[i+1]
    arr2.append(result)

print(tuple(arr2))

    