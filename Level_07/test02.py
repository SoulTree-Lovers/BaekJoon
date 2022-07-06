# 벌집

n = int(input())

start = 1
count = 2
x = 6
while 1:
    if n == 1:
        print(1)
        break
    if start < n <= start + x:
        print(count)
        break
    start += x 
    x += 6
    count += 1
    