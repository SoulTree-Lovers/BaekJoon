# 평균은 넘겠지

n = int(input())

average_list = []

for i in range(n):
    num_list = list(map(int, input().split(" ")))
    sum = 0
    average = None
    for j in range(1, num_list[0]+1):
        sum += num_list[j]
    average = sum / num_list[0]

    count = 0
    for j in range(1, num_list[0]+1):
        if num_list[j] > average:
            count += 1
    average_list.append(count/num_list[0] * 100)

for i in range(n):
    print("{:.3f}%".format(round(average_list[i], 3)))
