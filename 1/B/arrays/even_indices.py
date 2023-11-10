n = int(input())
lts = list(map(int, input().split()))

for i in range(0, n):
    if i % 2 == 0:
        print(lts[i])
