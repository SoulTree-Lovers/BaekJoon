# 소수 찾기 (1978)

n = int(input())
num_list = list(map(int, input().split(" ")))

count = 0

for i in num_list:
    boolean = True
    if i < 2:
        boolean = False

    for j in range(i-1, 1, -1):
        if i % j == 0:
            boolean = False

    if boolean == True:
        count += 1

print(count)

    