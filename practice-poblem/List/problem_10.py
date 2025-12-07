matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [[row[y] for row in matrix]for y in range(3)]

print(result)