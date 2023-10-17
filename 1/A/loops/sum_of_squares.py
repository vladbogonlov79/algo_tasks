number = int(input())
sum = 0
if number < 101:
    for i in range(1, number + 1):
        i = i ** 2
        sum += i
    else:
        print(sum)
