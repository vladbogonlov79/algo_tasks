st = input()
for i in range(len(st)):
    for j in range(i + 1, len(st)):
        if st[i] == st[j]:
            print(st[i])


