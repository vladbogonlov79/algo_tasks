n = int(input())
lts = list(map(int, input().split()))
max = lts[0]

for i in range(1, n):
    if lts[i] > max:
        max = lts[i]

print(max)
