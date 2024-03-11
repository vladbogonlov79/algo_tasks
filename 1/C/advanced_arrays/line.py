number_students = int(input())
student_growth = [int(s) for s in input().split()]
Petya_height = int(input())

count = len(student_growth) + 1
for i in range(len(student_growth)):
    if Petya_height > student_growth[i]:
        count = i + 1
        break

print(count)
