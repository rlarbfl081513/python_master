import sys
sys.stdin = open("input.txt")

# 8:54

# n*n 격자칸이 있다
# 터트릴 때 최대로 얻는 경우와 최소를 구해서 차이를 구하라

# ## 내가 짠 코드
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#     pre_max_way = float('-inf')
#     pre_min_way = float('inf')
#
#     # 그냥 처음부터 다 터트려보면서 가장 큰 값과 작은 값을 구하는 거임
#     for i in range(n):
#         for j in range(n):
#             max_way = 0
#             max_way += arr[i][j]
#             for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
#                 ny,nx = i+y,j+x
#                 while 0 <= ny < n and 0 <= nx < n:
#                         max_way += arr[ny][nx]
#                         ny,nx = ny+ y,nx + x
#
#             pre_max_way = max(pre_max_way, max_way)
#             pre_min_way = min(pre_min_way, max_way)
#
#     print(f'#{tc}',pre_max_way-pre_min_way)



## gpt가 좀 더 나은 버전으로 수정해준거

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    pre_max_way = float('-inf')
    pre_min_way = float('inf')

    for i in range(n):
        for j in range(n):
            total = arr[i][j]
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                for step in range(1, n):
                    ny, nx = i + dy * step, j + dx * step
                    if 0 <= ny < n and 0 <= nx < n:
                        total += arr[ny][nx]
                    else:
                        break
            pre_max_way = max(pre_max_way, total)
            pre_min_way = min(pre_min_way, total)

    print(f'#{tc}', pre_max_way - pre_min_way)
