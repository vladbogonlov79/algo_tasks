length = int(input())
mass = list(map(int, input().split()))

for i in range(0, length):
    if mass[i] % 2 == 0:
        print(mass[i])
