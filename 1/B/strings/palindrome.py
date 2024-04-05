mystring = list(input())
s = []
for i in range(len(mystring) - 1, -1, -1):
    s.append(mystring[i])
if mystring == s:
    print("yes")
else:
    print("no")



