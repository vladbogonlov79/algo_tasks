def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)

print(Fib(int(input())))


