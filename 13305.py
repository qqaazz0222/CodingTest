# 백준 13305번 문제

amount_city = int(input())
distance_between = input().split()
price_city = input().split()
min_price = int(price_city[0])
res = 0
for i in range(amount_city - 1):
    if (int(price_city[i]) < min_price):
        min_price = int(price_city[i])
    res += min_price * int(distance_between[i])
print(res)