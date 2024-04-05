k = input()
a = 0
b = []

for i in k:
    ord(i)
    if ord(i) >= 97 and ord(i) <= 122:
        a = ord(i) - 32
        b.append(chr(a))
    else:
        b.append(chr(ord(i)))

print("".join(b))
