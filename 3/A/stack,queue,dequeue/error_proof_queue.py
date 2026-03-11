queue = []

while True:
    command = input().split()

    if command[0] == "push":
        number = int(command[1])
        queue.append(number)
        print("ok")
    elif command[0] == "pop":
        if not queue:
            print("error")
        else:
            value = queue.pop(0)
            print(value)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "front":
        if not queue:
            print("error")
        else:
            print(queue[0])
    elif command[0] == "clear":
        queue.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break