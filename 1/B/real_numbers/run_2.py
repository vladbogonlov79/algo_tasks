inp = list(map(float, input().split()))

if len(inp) == 1:
    mileage = inp[0]
    distance = int(input())
else:
    mileage, distance = inp

total_mileage = mileage
days = 1
eps = 0.000001

while distance - total_mileage > eps and total_mileage < distance:
    mileage += mileage * 0.7
    total_mileage += mileage
    days += 1

print(days)
