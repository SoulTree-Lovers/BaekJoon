# 다이얼

two = "ABC"
three = "DEF"
four = "GHI"
five = "JKL"
six = "MNO"
seven = "PQRS"
eight = "TUV"
nine = "WXYZ"

str = input()

min_time = 0

for i in range(len(str)):
    if str[i] in two:
        min_time += 3
    elif str[i] in three:
        min_time += 4
    elif str[i] in four:
        min_time += 5
    elif str[i] in five:
        min_time += 6
    elif str[i] in six:
        min_time += 7
    elif str[i] in seven:
        min_time += 8
    elif str[i] in eight:
        min_time += 9
    elif str[i] in nine:
        min_time += 10

print(min_time)
