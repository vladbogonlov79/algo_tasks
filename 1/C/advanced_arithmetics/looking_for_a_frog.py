k, t = map(int, input().split())

n = t % (2 * k)
odd = ((t// k ) % 2)
ans = odd * (2 * k - n ) + (1 - odd) * n

print(ans)
