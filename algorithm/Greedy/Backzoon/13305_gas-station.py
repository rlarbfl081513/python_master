

city = int(input())
way_length = list(map(int,input().split()))
price = list(map(int,input().split()))

min_price = price[0]
total_cost = 0

# 앞에서부터, 더 싼 가격이 나올 때까지 현재 가격으로 계속 간다
for i in range(city-1):
    if price[i] < min_price:
        min_price = price[i]

    total_cost += min_price*way_length[i]

print(total_cost)