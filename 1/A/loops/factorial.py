number = int(input())
if number < 13:
    factorial = 1
    for i in range(1, number + 1):
         factorial *= i
    else:
         print(factorial)
