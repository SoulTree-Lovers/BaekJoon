# 단어의 개수

str = input().split(" ")
while 1:
    if "" in str:
        str.remove("")
    else:
        break
print(len(str))