a, b = map(int, input().split())
x, y = a, b

while y != 0:
    x, y = y, x % y

c = a // x
d = b // x

print(c, d)
