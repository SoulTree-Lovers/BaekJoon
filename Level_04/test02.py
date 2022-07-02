# 최댓값

num_list = []

for _ in range(9):
    num_list.append(int(input()))

max = max(num_list)
index = num_list.index(max) + 1


print(max)
print(index)