# OX 퀴즈

n = int(input())
str_list = []

for i in range(n):
    str_list.append(input())
    
for i in range(n):
    count = 0
    score = 0
    for j in range(len(str_list[i])):
        if str_list[i][j] == "O":
            count += 1
            score += count
        elif str_list[i][j] == "X":
            count = 0
    print(score)
        