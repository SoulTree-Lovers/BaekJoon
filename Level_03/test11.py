# X보다 작은 수
import sys

a, b = map(int, sys.stdin.readline().split(" "))

num_list = sys.stdin.readline().split(" ")
print_list = []

for i in range(a):
    if b > int(num_list[i]):
        print_list.append(int(num_list[i]))

for i in range(len(print_list)):
    print(print_list[i])
