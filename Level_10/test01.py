# 블랙잭 (2798)
import sys
from itertools import combinations, permutations


n, m = map(int, sys.stdin.readline().split(" "))

num_list = list(map(int, sys.stdin.readline().strip().split(" ")))

test_list = []

for i in combinations(num_list, 3):
    test_list.append(sum(i))

test_list.sort()

min = m - test_list[0]
value = test_list[0]

for i in test_list:
    if 0 <= m - i <= min:
        min = m - i
        if i <= m:
            value = i

print(value)
