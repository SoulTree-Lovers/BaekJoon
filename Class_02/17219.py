# 비밀번호 찾기

import sys

n, m = map(int, sys.stdin.readline().split())

site_dict = {}

for i in range(n):
    site, pw = map(str, sys.stdin.readline().split())
    
    site_dict[site] = pw

print_list = []

for i in range(m):
    search = sys.stdin.readline().rstrip()
    print_list.append(site_dict[search])

for i in print_list:
    print(i)