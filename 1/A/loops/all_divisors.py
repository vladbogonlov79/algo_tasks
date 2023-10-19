divisible = int(input())

for i in range(1, divisible + 1):
    if divisible % i == 0:
        print(i)