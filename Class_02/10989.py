# 수 정렬하기 3
import sys

num = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(num):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()

for i in num_list:
    print(i)