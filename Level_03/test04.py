# 빠른 A + B
import sys

n = int(input())
num_list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split(" "))
    num_list.append(a + b)

for i in range(n):
    print(num_list[i])
