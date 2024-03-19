n = int(input())
nums = list(map(int, input().split()))
maximum = nums[0]
a = 1

for i in range(1, n):
    if nums[i] > maximum:
        maximum = nums[i]
        a = i + 1

print(a)
