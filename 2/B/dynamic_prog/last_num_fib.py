n = int(input())  
a = [1, 1] 

for i in range(2, n + 1):  
    a += [a[-1] + a[-2]]  
print(str(a[-1])[-1])
