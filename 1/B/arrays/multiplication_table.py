rows, column = map(int, input().split())
lis = [[0] * column for _ in range(rows)]

for i in range(rows):
    for j in range(column):
        lis[i][j] = i * j

for i in lis:
    print(*i)
