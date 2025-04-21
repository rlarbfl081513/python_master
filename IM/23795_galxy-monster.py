import sys
sys.stdin = open("input.txt")

# 8:00

# n*n의 배열
# 괴물은 벽에 닿지 않는 이상 광선을 계속해서 뻗어낸다. 안전한 빈칸의 수를 구하라
# 0은 빈칸, 1은 벽, 2는 괴물


## 내가 짠 비효율적 : 스택으로 dfs느낌으로 푼 코드
## 논리적으로 잘못된건 아님 -> 과하다고 gpt가 말함
#
# delta = [(0,-1),(0,1),(1,0),(-1,0)]
#
# def monster(start_y,start_x):
#     global kill
#
#     for k in range(4):
#         n_y,n_x = start_y+delta[k][0],start_x+delta[k][1]
#         stack = [(n_y,n_x)]
#         while stack:
#             next_y,next_x = stack.pop()
#             if 0 > next_y or n <= next_y or 0 > next_x or n <= next_x:
#                 break
#             if arr[next_y][next_x] == 1:
#                 break
#             stack.append((next_y+delta[k][0],next_x+delta[k][1]))
#             kill += 1
#
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#
#     mon_y,mon_x = 0,0
#     wall = 1
#
#     # 일단 괴물의 위치를 찾는다
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 2:
#                 mon_y, mon_x = i,j
#             if arr[i][j] == 1:
#                 wall += 1
#     kill = 0
#     monster(mon_y,mon_x)
#     map_arr = n*n
#     total = map_arr -wall - kill
#
#     print(f'#{tc} {total}')



## gpt가 효율적으로 짜준 코드

def monster(start_y,start_x):
    global kill

    for dy,dx in [(0,-1),(0,1),(1,0),(-1,0)]:
        ny,nx = start_y+dy, start_x+dx
        while 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1:
            ny += dy
            nx += dx
            kill += 1


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    mon_y,mon_x = 0,0
    wall = 1

    # 일단 괴물의 위치를 찾는다
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                mon_y, mon_x = i,j
            if arr[i][j] == 1:
                wall += 1
    kill = 0
    monster(mon_y,mon_x)
    map_arr = n*n
    total = map_arr - wall - kill

    print(f'#{tc} {total}')