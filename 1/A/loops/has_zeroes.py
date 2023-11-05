numbers = int(input())
quantity = -1
zeros = 0

for i in range(numbers):
    quantity = int(input())
    if quantity == 0:
        zeros += 1
if zeros > 0:
    print("YES")

else:
    print("NO")


