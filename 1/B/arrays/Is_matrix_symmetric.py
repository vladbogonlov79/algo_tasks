n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
flag = True
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
if flag:
    print("yes")
else:
    print("no")
