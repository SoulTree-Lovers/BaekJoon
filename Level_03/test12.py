# A + B - 5
import sys

num_list = []

while 1:
    a, b = map(int, sys.stdin.readline().split(" "))

    if a == b == 0:
        break;

    num_list.append(a + b)

for i in range(len(num_list)):
    print(num_list[i])
        
    
    