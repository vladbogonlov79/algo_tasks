#первый момент времени
time = int(input()) * 3600
time += int(input()) * 60
time += int(input())
# второй момент времени
time_two = int(input()) * 3600
time_two += int(input()) * 60
time_two += int(input())
time = time_two - time

print(time)