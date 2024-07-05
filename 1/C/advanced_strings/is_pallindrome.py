lin = input()
lin = lin.replace(' ', '')
if lin == lin[::-1]:
    print('yes')
else:
    print('no')
