# 덱

import sys

num = int(sys.stdin.readline().rstrip())

deque = []

for i in range(num):
    input = sys.stdin.readline().rstrip().split()

    if input[0] == "push_front":
        deque.insert(0, input[1])
    elif input[0] == "push_back":
        deque.append(input[1])
    elif input[0] == "pop_front":
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif input[0] == "pop_back":
        if len(deque) != 0:
            print(deque.pop(-1))
        else:
            print(-1)
    elif input[0] == "size":
        print(len(deque))
    elif input[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif input[0] == "back":
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)