# 소수 (2581)

a = int(input())
b = int(input())

min_list = []

for i in range(a, b+1):
    boolean = True
    if i < 2:
        boolean = False
    for j in range(2, i): # 1과 자기 자신 사이의 수로 나누었을 때 0이 나오면 False
        if i % j == 0:
            boolean = False
    if boolean == True:
        min_list.append(i)

if len(min_list) == 0:
    print(-1)
else:
    print(sum(min_list))
    print(min_list[0])