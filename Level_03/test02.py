# A + B 출력하기

test_num = int(input())
num_list = []

for i in range(test_num):
    num = input().split(" ")
    num_list.append(int(num[0]) + int(num[1]))

for i in range(test_num):
    print(num_list[i])