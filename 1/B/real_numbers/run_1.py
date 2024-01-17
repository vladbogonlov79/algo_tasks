mileage, distance = map(float, input().split())
days = 1
eps = 0.000001
while distance - mileage > eps and mileage < distance:
    mileage += mileage * 0.7
    days += 1
print(days)
