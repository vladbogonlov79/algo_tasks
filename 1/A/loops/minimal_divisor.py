number = int(input())
divisor = 1

while divisor <= number:
    divisor += 1
    if number % divisor == 0:
        break
print(divisor)
