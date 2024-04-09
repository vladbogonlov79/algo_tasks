mystring = list(input())
a = -1 
flag = True
for i in range (0, len(mystring)):
    if mystring[i] == mystring[a]:
        a += -1
        flag = True
    else :
        flag = False
        print('no')
        break 
if flag == True:
    print('yes')



