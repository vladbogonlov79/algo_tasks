def fib(num: int, memory: dict):
    if  num in memory:
        return memory[num]
    elif  num <= 2 :
        return 1
    result = fib(num = num - 1, memory = memory)+fib(num = num-2,memory=memory)
    memory[num] = result
    return result

num = int(input())
print(fib(num, memory={}))
