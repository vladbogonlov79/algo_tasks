children, adults, k = (int(i) for i in input().split())

buses = (children + adults) / k
if buses != int(buses):
    buses = int(buses) + 1
if buses <= adults / 2:
    print(int(buses))
else:
    print(0)
    