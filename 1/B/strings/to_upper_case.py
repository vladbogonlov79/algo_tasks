s = input()
ch = 0
ls = []

for i in s:
    ord(i)
    if ord(i) >= 97 and ord(i) <= 122:
        ch = ord(i) - 32
        ls.append(chr(ch))
    else:
        ls.append(i)

print("".join(ls))
