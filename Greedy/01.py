# 백준 5585번 거스름돈
pay = int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0
pay = 1000 - pay
for coin in coins:
    count += pay // coin
    pay = pay % coin
print(count)
