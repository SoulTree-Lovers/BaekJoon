# 수 정렬하기 3
import sys

num = int(sys.stdin.readline().rstrip())

count = [0] * 10001

for i in range(num):
    n = int(sys.stdin.readline())
    count[n] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)