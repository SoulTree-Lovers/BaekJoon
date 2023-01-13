# 미완성

count_0 = 0
count_1 = 0

def fibo(n, fib):
    global count_0
    global count_1
    if n == 0:
        count_0 += 1
    elif n == 1:
        count_1 += 1
    else:
        fibo(n-1)
        fibo(n-2)

n = int(input())
nums = []
fib = []
for i in range(n):
    nums.append(int(input()))

for i in nums:
    fibo(i, fib)
    print(count_0, count_1)
    count_0 = 0
    count_1 = 0