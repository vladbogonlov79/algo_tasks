equation = input()
number = ''

for char in equation:
    if char.isdigit():
        number += char
    else:
        if number and int(number) > 5:
            print("NO")
            break
        number = ''
else:
    if number and int(number) > 5:
        print("NO")
    else:
        print("YES")