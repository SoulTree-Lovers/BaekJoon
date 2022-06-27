# 알람 시계
time = input().split(" ")

hour = int(time[0])
minute = int(time[1])

if minute - 45 >= 0:
    print(hour, minute - 45)
elif minute - 45 < 0:
    if hour - 1 >= 0:
        print(hour-1, minute + 15)
    else:
        print(23, minute + 15)