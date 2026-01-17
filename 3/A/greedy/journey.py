dist,l_tank = map(int,input().split())
stations = int(input())
way = list()
for _ in range(stations):
    a = list(map(int,input().split()))
    way.append(a)

print(dist,l_tank)
print(stations,*way)
