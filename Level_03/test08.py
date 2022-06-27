# A + B (8)

import sys

n = int(input())
num_list = []

for i in range(n):
    num_list.append(list(map(int, sys.stdin.readline().split(" "))))

for i in range(n):
    print("Case #{}: {} + {} = {}".format(i+1, num_list[i][0], num_list[i][1], num_list[i][0] + num_list[i][1]))