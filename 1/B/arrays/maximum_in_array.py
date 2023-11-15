n = int(input())
lts = list(map(int, input().split()))
quantity = 0
max = lts[0]

for i in range(1, n):
    if lts[i] > max:
        max = lts[i]

print(max)
