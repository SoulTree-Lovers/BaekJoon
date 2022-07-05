# 상수의 숫자 구별법

num_list = list(map(int, input().split(" ")))

num1 = ""
num2 = ""
for i in range(2, -1, -1):
    num1 += str(num_list[0])[i]
    num2 += str(num_list[1])[i]
    
if int(num1) > int(num2):
    print(int(num1))
else:
    print(int(num2))