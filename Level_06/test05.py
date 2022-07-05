# 단어 공부

str = input().upper()
str_2 = list(set(str))

count_dict = dict()

for i in range(len(str_2)):
    count_dict[str_2[i]] = str.count(str_2[i])

if list(count_dict.values()).count(max(count_dict.values())) > 1:
    print("?")

else:
    reverse_dict = {v:k for k,v in count_dict.items()}
    print(reverse_dict[max(count_dict.values())])

