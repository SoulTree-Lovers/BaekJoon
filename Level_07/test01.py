# 손익분기점

x = list(map(int, input().split(" ")))

fixed_expenditure = x[0]
production_cost = x[1]
amount = x[2]

if production_cost < amount:
    print(int(fixed_expenditure / (amount - production_cost) + 1))
else:
    print(-1)
    