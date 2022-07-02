# 나머지

num_list = []

for i in range(10):
    num_list.append(int(input()))

for i in range(10):
    num_list[i] = num_list[i] % 42

num_list = set(num_list)

print(len(num_list))