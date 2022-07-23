# 골드바흐의 추측 (9020)
import sys
import math
# 소수 판별 함수
def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

prime_list = [i for i in range(2, 10000) if is_prime_number(i) == True]

n = int(sys.stdin.readline())

num_list = []

for i in range(n):
    even = int(sys.stdin.readline())
    half = even // 2

    for i in range(half, 1, -1):
        if i in prime_list and even - i in prime_list:
            num_list.append([i, even - i])
            break
    

for i in range(n):
    print(num_list[i][0], num_list[i][1])