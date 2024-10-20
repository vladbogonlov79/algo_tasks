py.
a, b, a2, b2 = map(int, input().split())
x = abs(a - a2)
y = abs(b - b2)
c = x
e = y

while y != 0:
    x, y = y, x % y

d = x

print(d * (c//d + e//d - 1))
