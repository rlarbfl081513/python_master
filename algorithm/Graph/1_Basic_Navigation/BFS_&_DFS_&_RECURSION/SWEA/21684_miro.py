import sys
sys.stdin = open("input.txt")

# 재귀함수에서의 return
# 재귀함수를 돌릴때는 return으로 함수가 바로 끝날수는 없다. 재귀를 통해 몇번째로 들어간 해당 함수 하나만 종료되는 것이다.
# 때문에 반환하고 싶은 값이 있으면 계속해서 전파시키거나, 변수를 설정하여 변수에 할당하는 숫자를 반환값으로 바꾸어 최종적을 변수를 출력하게 할 수도 있다.


# 재귀
# def recursion_miro(start_y,start_x):
#     global arr,res
#
#     # 아래의 코드와 포문안의 코드 중 하나만 사용하면 되는 거임
      # 원하는 숫자에 도달했다는 것을 res라는 변수에 할당하는 숫자를 바꿈으로 알려주는 거니까
#     # if arr[start_y][start_x] == 3:
#     #     return 1
#     # visit[start_y][start_x] = True
#
#     for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:
#         ny,nx = start_y+y,start_x+x
#         if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visit[ny][nx] == False:
#             visit[ny][nx] = True
#             if arr[ny][nx] == 3:
#                 res = 1
#                 return
#             recursion_miro(ny, nx)

# 1만 아니면 갈 수 있는 길이라고 하고 만들기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(n)]
#     visit = [[False]*n for _ in range(n)]
#     y,x = 0,0
#     res = 0
#     for i in range(n):
#         for j in range(n):
#             # 출발지
#             if arr[i][j] == 2:
#                 y,x = i,j
#
#     recursion_miro(y,x)
#     print(f'#{tc} {res}')



## 재귀 : 굉장히 잘못된 코드
# 재귀함수로서 리턴에 대한 이해도가 잘못되었을떄의 상황
# 사실상 함수가 아닌 출력방식만 2번 방식으로 바꾸면 되는 거였음, 하지만 아래에서 말하는 1번방식으로 출력을 하고싶다면 함수를 고쳐야함
# def recursion_miro(start_y,start_x):
#     global arr, res
#
#     # 1번 방식의 출력은 최종적으로 함수가 끝날때 반환되는 값을 프린트하는 것이다.
#     # 현재는 재귀함수로서 아래 코드에서 리턴한다고 바로 다 끝나고 1이 출력되는게 아니가
#     # 재귀로 불린 몇번째인가의 함수가 끝났다는 거고, 반환되는 1이라는 숫자도 해당 함수만의 반환값인것이다
#     # 때문에 반환받은 값을 계속 앞의 재귀함수들한테도 전달해야. 최종적인 함수가 끝날때 해당 반환값을 내보낸다.
#     if arr[start_y][start_x] == 3:
#         res = 1
#         return 1
#     visit[start_y][start_x] = True
#
#     for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:
#         ny,nx = start_y+y,start_x+x
#         if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visit[ny][nx] == False:
#             visit[ny][nx] = True
#
#             # 2번 방식이면 아래처럼만 해도됨
#             # recursion_miro(ny,nx)
#
#             # 1번 방식이면 아래처럼 리턴받은 값은 계속 전파시킴
#             result = recursion_miro(ny, nx)
#             if result == 1:
#                 return 1  # 여기
#
#
# # 1만 아니면 갈 수 있는 길이라고 하고 만들기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(n)]
#     visit = [[False]*n for _ in range(n)]
#     y,x = 0,0
#     res = 0
#     for i in range(n):
#         for j in range(n):
#             # 출발지
#             if arr[i][j] == 2:
#                 y,x = i,j
#
#     # 1번 방식 출력 ; 아래와 같은 형식으로 값을 받고 싶으면 위의 함수를 고쳐야하는 거였고
#     print(recursion_miro(y,x))
#
#     # 2번 방식 출력 : 아래와 같이 출력값을 받는다면 위의 함수는 사실상 문제가 없던거임
#     recursion_miro(y, x)
#     print(res)




# # 큐를 통한 bfs
# from collections import deque
#
# def recursion_miro(start_y,start_x):
#     global arr
#
#     visit[start_y][start_x] = True
#     q = deque()
#     q.append((start_y,start_x))
#
#     while q:
#         start_y, start_x = q.popleft()
#
#         if arr[start_y][start_x] == 3:
#             return print(f'#{tc}',1)
#
#         for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:
#             ny,nx = start_y+y,start_x+x
#             if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visit[ny][nx] == False:
#                 visit[ny][nx] = True
#                 q.append((ny,nx))
#
#
#     return print(f'#{tc}',0)
#
# # 1만 아니면 갈 수 있는 길이라고 하고 만들기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(n)]
#     visit = [[False]*n for _ in range(n)]
#     y,x = 0,0
#     for i in range(n):
#         for j in range(n):
#             # 출발지
#             if arr[i][j] == 2:
#                 y,x = i,j
#
#     recursion_miro(y,x)



# # 스택으로 풀기
#
# def stack_miro(start_y,start_x):
#     global arr
#
#     visit[start_y][start_x] = True
#     stack = []
#     stack.append((start_y,start_x))
#
#     while stack:
#         start_y, start_x = stack.pop()
#
#         if arr[start_y][start_x] == 3:
#             return print(f'#{tc}',1)
#
#         for y,x in [(0,1),(1,0),(0,-1),(-1,0)]:
#             ny,nx = start_y+y,start_x+x
#             if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visit[ny][nx] == False:
#                 visit[ny][nx] = True
#                 stack.append((ny,nx))
#
#     return print(f'#{tc}',0)
#
# # 1만 아니면 갈 수 있는 길이라고 하고 만들기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(n)]
#     visit = [[False]*n for _ in range(n)]
#     y,x = 0,0
#     for i in range(n):
#         for j in range(n):
#             # 출발지
#             if arr[i][j] == 2:
#                 y,x = i,j
#
#     stack_miro(y,x)
#     print(path)



# 재귀인데 경로 추적까지
# dfs로 경로 추적시에는 백트래킹 처리를 해줘야 깔끔한 경로가 나옴

def recursion_miro(start_y,start_x):
    global arr,res,path
    visit[start_y][start_x] = True


    for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:
        ny,nx = start_y+y,start_x+x
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 1 and visit[ny][nx] == False:

            visit[ny][nx] = True

            if arr[ny][nx] == 3:
                res = 1
                return True  # 찾음

            path.append((ny, nx))

            found = recursion_miro(ny, nx)
            if found:
                return True  # 찾은 경로면 유지
            path.pop()  # 백트래킹: 실패한 경로 제거

    return False  # 모든 방향 실패

# 1만 아니면 갈 수 있는 길이라고 하고 만들기
t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(n)]
    visit = [[False]*n for _ in range(n)]
    path = []
    y,x = 0,0
    res = 0
    for i in range(n):
        for j in range(n):
            # 출발지
            if arr[i][j] == 2:
                y,x = i,j
                path.append((y,x))

    recursion_miro(y,x)
    print(f'#{tc} {res}')
    print(path)