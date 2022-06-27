# 더하기 사이클

first_n = input()

new_n = first_n

if len(new_n) == 1:
    new_n = "0" + new_n
    first_n = "0" + first_n
add = str(int(new_n[0]) + int(new_n[1]))

new_n = new_n[1] + add[-1]
count = 1


while first_n != new_n:
    add = str(int(new_n[0]) + int(new_n[1]))
    new_n = new_n[1] + add[-1]
    count += 1
    
print(count)
    

