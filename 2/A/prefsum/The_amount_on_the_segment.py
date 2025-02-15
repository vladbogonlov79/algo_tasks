length, requests = map(int, input().split())
array = list(map(int, input().split()))
prefix_sums = [0] * (length + 1)
answers = []

for i in range(length):
    prefix_sums[i + 1] = prefix_sums[i] + array[i]

for _ in range(requests):
    x, y = map(int, input().split())
    t = prefix_sums[y] - prefix_sums[x - 1]
    answers.append(t)

for element in answers:
    print(element)
