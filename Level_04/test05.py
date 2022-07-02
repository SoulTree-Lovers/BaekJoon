# 평균

n = int(input())
num_list = list(map(int, input().split(" ")))

max = max(num_list)

for i in range(n):
    num_list[i] = num_list[i] / max * 100

sum = 0
for i in range(n):
    sum += num_list[i]

print(sum / n)
