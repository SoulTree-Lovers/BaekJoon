# 최소, 최대

n = int(input())
num_list = list(map(int, input().split(" ")))


max = num_list[0]
min = num_list[0]
for i in range(n):
    if max < num_list[i]:
        max = num_list[i]
    if min > num_list[i]:
        min = num_list[i]
    
print(min, max)
