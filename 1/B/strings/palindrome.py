mystring = list(input())
flag = False

for i in range(0, len(mystring)):
    if mystring[i] == mystring[-i-1]:
        flag = True
    else:
        flag = False
        print('no')
        break
if flag == True:
    print('yes')
