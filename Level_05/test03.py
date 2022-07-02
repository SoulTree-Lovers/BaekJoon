# 한수

num = int(input())

count = 0

for n in range(1, num+1):
    if len(str(n)) > 2:
        x = int(str(n)[1]) - int(str(n)[0])    

        if x != int(str(n)[2]) - int(str(n)[1]):
            count -= 1

    count += 1

print(count)

