# 오븐 시계

current_time = input().split(" ")
oven_time = int(input())

hour = int(current_time[0])
minute = int(current_time[1])

if minute + oven_time < 60:
    print(hour, minute + oven_time)
else: 
    while minute + oven_time >= 60:
        hour += 1
        oven_time -=60

        if hour > 23:
            hour = 0
            
    print(hour, minute + oven_time)
