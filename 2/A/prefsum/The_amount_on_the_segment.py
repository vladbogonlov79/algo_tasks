n, m = map(int, input().split())
array = list(map(int, input().split()))
prefix_sums = [0] * (n + 1)
q = []
for i in range(n):
    prefix_sums[i + 1] = prefix_sums[i] + array[i]

for _ in range(m):
    x, y = map(int, input().split())
    t = prefix_sums[y] - prefix_sums[x - 1]
    q.append(t)

for element in q:
    print(element)
