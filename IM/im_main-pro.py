import sys
sys.stdin = open("input.txt")

# 12:00

## 문제 : 현주 상자
# 현주는 1~n번 상자 가짐, 처음에는 다 0 적힘
# q회동안 i번째 작업에서  l~r상자를 i로 값 변경

# t = int(input())
# for tc in range(1,1+t):
#     n,q = map(int,input().split())
#     box = [0]*(n+1)
#     # print(box)
#
#     for i in range(1,1+q):
#         a,b = map(int,input().split())
#         for j in range(a,b+1):
#             box[j] = i
#
#     box = box[1:]
#     print(f'#{tc}', " ".join(list(map(str,box))))


# t = int(input())
# for tc in range(1,1+t):
#     n,q = map(int, input().split())
#     arr = [0]*n
#     for i in range(1,1+q):
#         l,r = map(int,input().split())
#         for j in range(l-1,r+1-1):
#             arr[j] = i
#
#     print(f'#{tc} {" ".join(list(map(str,arr)))}')



## 괴물
# 12:19 - 12:36
# n*n
# 빈칸 0, 벽 1, 괴물 2

# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#
#     mon_y,mon_x = 0,0
#     brick = 0
#     # 괴물 찾기
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 2:
#                 mon_y, mon_x = i,j
#             if arr[i][j] == 1:
#                 brick += 1
#
#     cnt = 0
#     for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
#         way = 1
#         while True:
#             ny,nx = mon_y+y*way,mon_x+x*way
#             if 0 > ny or ny >= n or 0 > nx or nx >= n:
#                 break
#             if arr[ny][nx] == 1:
#                 break
#             cnt += 1
#             way += 1
#
#     print(f'#{tc} {n*n-cnt-brick-1}')


## 돌 뒤집기
# 12:36

# i번째의 돌을 사이에 두고 마주보는 j개의 돌에개해 같으면 뒤집고 아니면 그대로 두고
# n 돌의수, m 뒤집기 횟수
# n개의 돌 상태
# m개의 줄에 i.j 주어짐
# 시작 수는 1로

# def stoto(a,b,arr):
#     a = a-1
#     for k in range(1,b+1):
#         if 0 > a+1*k or n <= a+1*k or 0 > a-1*k or n <= a-1*k:
#             return
#
#         if arr[a+1*k] == arr[a-1*k]:
#             arr[a + 1 * k] = 1 - arr[a+1*k]
#             arr[a - 1 * k] = 1 - arr[a - 1 * k]
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n,m = map(int,input().split())
#     stone = list(map(int,input().split()))
#     for i in range(m):
#         a,b = map(int,input().split())
#         stoto(a,b,stone)
#
#
#     print(f'#{tc}'," ".join(list(map(str,stone))))



## 풍선팡 게임

# n*n 격자판 있음
# 터트려서 가장 큰 값과 가장 작은 값을 구해서 빼라

t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    max_num = float('-inf')
    min_num = float('inf')

    for i in range(n):
        for j in range(n):
            cnt = 0
            cnt += arr[i][j]
            for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
                way = 1
                while True:
                    ny,nx = i+y*way,j+x*way
                    if 0 > ny or n <= ny or 0 > nx or n <= nx:
                        break

                    cnt += arr[ny][nx]
                    way += 1

            max_num = max(max_num,cnt)
            min_num = min(min_num, cnt)

    print(f'#{tc} {max_num-min_num}')