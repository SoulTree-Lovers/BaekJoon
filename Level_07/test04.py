# 달팽이는 올라가고 싶다 (2869)
import math 

num_list = list(map(int, input().split(" ")))

a = num_list[0]
b = num_list[1]
v = num_list[2]

day = math.ceil((v - b) / (a - b))

print(day)


