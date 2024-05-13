integer = int(input())
valid_num = float(input())
sum = 1
mul = 1

for i in range(1, integer + 1):
    mul *= valid_num
    sum += mul

print(sum)
