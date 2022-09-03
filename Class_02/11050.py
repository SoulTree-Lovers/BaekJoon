# 이항 계수 1

import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split(" "))

print(int(factorial(n) / (factorial(k) * factorial(n-k))))