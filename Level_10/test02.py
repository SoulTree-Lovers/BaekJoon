# 분해합 (2231)


def divideSum(n):
    sum = n
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    return sum
    
n = int(input())

array = {}

x = 1
while divideSum(x) <= 1000:
    if divideSum(x) not in array:
        array[divideSum(x)] = [x]
    else:
        array[divideSum(x)].append(x)
    x += 1

if n in array:
    print(min(array[n]))
else:
    print(0)