# 설탕 배달

n = int(input())
    
ret = None

for five in range(1001):
    for three in range(1668):
        if 5 * five + 3 * three == n:
            ret = five, three
        
if ret == None:
    print(-1)
else:
    print(sum(ret))