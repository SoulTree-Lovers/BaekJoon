# 부녀회장이 될테야 (2775)

memo = {}
def people(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1
    if (k, n) in memo:
        return memo[(k, n)]
    else:
        output = people(k-1, n) + people(k, n-1)
        memo[(k, n)] = output
        return output
    



test_case = int(input())

print_list = []

for i in range(test_case):

    k = int(input())
    n = int(input())

    print_list.append(people(k, n))    

for i in range(test_case):
    print(print_list[i])
    