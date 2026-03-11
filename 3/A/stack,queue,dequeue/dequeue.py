deque = []
while True:
    command = input().split()

    if command[0] == "push_front":
        number = int(command[1])
        deque.insert(0,number)
        print("ok")
    elif command[0] == "push_back":
        number = int(command[1])
        deque.append(number)
        print("ok")
    elif command[0] == "pop_front":
        if not deque:
            print("error")
        else:
            value = deque.pop(0)
            print(value)
    elif command[0] == "pop_back":
        if not deque:
            print("error")
        else:
            value = deque.pop()
            print(value)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "front":
        if not deque:
            print("error")
        else:
            print(deque[0])
    elif command[0] == "back":
        if not deque:
            print("error")
        else:
            print(deque[-1])
    elif command[0] == "clear":
        deque.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break