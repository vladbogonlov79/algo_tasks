length = int(input())
mass = list(map(int, input().split()))
quantity = 0

for i in range(0, length):
    if i == 0:
        continue
    if mass[i - 1] < mass[i]:
        quantity += 1
print(quantity)
