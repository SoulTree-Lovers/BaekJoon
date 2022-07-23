# 베르트랑 공준 (4948) - PyPy3로 실행 (Python3는 시간 초과라고 뜸)
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

print_list = []

while 1:
    count = 0
    n = int(sys.stdin.readline().rstrip())
    
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if is_prime_number(i):
            count += 1
    print_list.append(count)

for i in range(len(print_list)):
    print(print_list[i])
