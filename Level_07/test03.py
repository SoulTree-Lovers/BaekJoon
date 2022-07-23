# 분수찾기 (1193)

n = int(input())

count = 0
line = 0

while count < n:
    line += 1
    count += line

count -= line

if line % 2 == 0:
    row = n - count
    col = line + 1 - row

else:
    col = n - count
    row = line + 1 - col


print("{}/{}".format(row, col))        