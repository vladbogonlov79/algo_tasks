nums = -1
maximum = 0
num_maximal = 0

while nums != 0:
    nums = int(input())
    if nums > maximum:
        maximum = nums
        num_maximal = 1
    elif nums == maximum:
        num_maximal += 1        
print(num_maximal)
