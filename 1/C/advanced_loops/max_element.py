n = int(input())
element = (int(s) for s in input().split())
maximum = -100
for i in element:
    if i > maximum:
        maximum = i

print(maximum)