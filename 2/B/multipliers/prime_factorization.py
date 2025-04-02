def smallest_div(n,d):
    for i in range(d, int(n ** 0.5 + 1)):
        if n % i == 0:
            return (i)
    return(n)

n = int(input())
d = 2
res = []

while n > 1:
    d = smallest_div(n,d)
    n = n // d
    res.append(str(d))

print('*'.join(res))
