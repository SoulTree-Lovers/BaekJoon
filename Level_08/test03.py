# 소인수분해 (11653)

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())



num_list = []

while not is_prime(n):
    j = 2
    while j < n:
        if n % j == 0:
            num_list.append(j)
            n = n // j
            continue
        j += 1


if n != 1:
    num_list.append(n)

for i in range(len(num_list)):
    print(num_list[i])
