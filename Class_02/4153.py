# 직각삼각형

import sys

print_list = []

while True:
    num_list = list(map(int, sys.stdin.readline().split(" ")))
    if num_list[:] == [0, 0, 0]:
        break

    num_list.sort()

    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        print_list.append("right")
    else:
        print_list.append("wrong")

for i in print_list:
    print(i)