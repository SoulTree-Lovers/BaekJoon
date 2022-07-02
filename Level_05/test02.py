# 셀프 넘버

def d(n):
    sum = 0
    sum += n
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum


num_list = [i for i in range(1, 10001)]
num_list_2 = []

for i in range(1, 10000):
    if d(i) <= 10000:
        num_list_2.append(d(i))

num_list_2 = set(num_list_2)
num_list_2 = list(num_list_2)

for i in range(len(num_list_2)):
    num_list.remove(num_list_2[i])

for i in range(len(num_list)):
    print(num_list[i])