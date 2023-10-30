numbers = int(input())
quantity = -1
if numbers == 0:
    print("Yes")
else:
    for i in range(numbers):
        quantity *= int(input())

    if quantity == 0:
        print("Yes")
    else:
        print("No")
