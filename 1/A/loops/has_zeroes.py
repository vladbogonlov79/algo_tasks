length = int(input())
was_zero = False

for _ in range(length):
    was_zero = was_zero or int(input()) == 0

if was_zero:
    print("YES")
else:
    print("NO")
