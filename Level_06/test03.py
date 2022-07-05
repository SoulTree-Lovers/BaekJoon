# 알파벳 찾기
abc = "abcdefghijklmnopqrstuvwxyz"

word = input()

for i in range(len(abc)):
    if abc[i] in word:
        print(word.find(abc[i]), end=" ")
    else:
        print(-1, end=" ")