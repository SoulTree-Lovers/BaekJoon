#  ACM 호텔 (10250)
import math

num = int(input())

num_list = []

for i in range(num):
    temp = list(map(int, input().split(" ")))
    num_list.append(temp)

print_list = []

for i in range(num):
    h = num_list[i][0] 
    w = num_list[i][1]
    n = num_list[i][2]

    x = str(n % h)
    y = str(math.ceil(n / h)).zfill(2)
    
    if x == "0":
        x = str(h)

    loc = x+y

    print_list.append(loc)

for i in range(num):
    print(int(print_list[i]))
