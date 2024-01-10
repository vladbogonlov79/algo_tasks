sum_ = float(input())
sum_ += float(input())
amount = float(input())
amount = amount - sum_
eps = 0.00000001
if abs(amount) < eps:
    print("YES")
else:
    print("NO")
