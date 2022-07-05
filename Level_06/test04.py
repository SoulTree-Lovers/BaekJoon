# 문자열 반복

n = int(input())

str_list = []

for i in range(n):
    test = input().split(" ")
    str = ""

    for j in range(len(test[1])):
        str += test[1][j] * int(test[0])         
    
    str_list.append(str)

for i in range(len(str_list)):
    print(str_list[i])