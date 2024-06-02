num = list(input())
a = []
n = 0
for i in range(len(num)-1, -1, -1):
    a += num[i]
    n += 1
    if n % 3 == 0:
        a.append(",")

print(''.join(a[::-1]).strip(','))

