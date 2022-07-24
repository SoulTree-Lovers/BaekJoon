# 피보나치 수 5 (10870)

def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1

    for i in range(n-2):
        a, b = b, a+b

    return b

n = int(input())

print(fibo(n))
