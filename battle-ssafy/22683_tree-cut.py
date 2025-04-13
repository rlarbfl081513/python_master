import sys
sys.stdin = open("input.txt")

# 나무베기
# 차윤이 : 앞, 왼으로 90도 회전, 오른 90도회전 rc카
# 출발에서 도착까지 최소의 조작으로 이동 -> 최단거리가 아닌 최소 리모컨 조작 횟수
# 회전하는것도 조작횟수에 포함되지만 이동하는거는아니라는 걸 알아두자

# 필드의 넓이
# 밸수 있는 나무의 수
# x : 출발지
# y : 도착지
# g 이동가능땅
# t 나무때문에 못가는 곳


## 버전_1. 방문 set()으로 구현
## 코드는 단순해지지만 속도가 느림
## 시간초과 나옴
    # set()에 넣는 튜플이 너무 많음 -> (조작수, 나무벤수, 위치yx,방향) 작은 변화도 다른 상태로 인식됨 -> 불필요하게 많은 중복산태 처리 발생
    # 힙큐를 사용해도 set을 통한 중복제거가 느려서 탐색 공간이 넓어질수록 효율이 떨어짐 --> 그래서 이문제는 4중포문으로 푸는거임 -> 그래야 비교하면서 추가하니까 불필요한 상태는 애초에 안넣고 안보는거임
# import heapq
#
# delta = [(-1,0),(0,1),(1,0),(0,-1)]
#
# def cut_tree(total,now_cut,start_y,start_x,dir):
#     global n, k, arr, visit, visited
#
#     q = [(total,now_cut,start_y,start_x,dir)]
#
#     while q:
#         # 전체 이동
#         result, cut ,now_y,now_x,dir = heapq.heappop(q)
#
#         if arr[now_y][now_x] == 'Y':
#             return result
#
#         # 직진 시 코드
#         dy,dx = delta[dir]
#         ny,nx = now_y+dy, now_x+dx
#         if 0 <= ny < n and 0 <= nx < n:
#             ncut = cut + 1 if arr[ny][nx] == 'T' else cut
#             state = (result+1, ncut, ny, nx, dir)
#             # visited set()으로 해당 좌표에서 해당 컷팅수+해당 방향+해당 총 조작 수로 간적이 있는지 판단
#             if ncut <= k and state not in visited:
#                 visited.add(state)
#                 # 해당 정보로 간적이 없었다면 큐에 추가
#                 heapq.heappush(q, (result+1, ncut, ny, nx, dir))
#
#         # 오른쪽 왼쪽 회전 시
#         # 회전한 방향으로 해서 나머지 정보들중 조작수만 1을 올리고 나머지는 그대로 다시 큐에 넣기
#         for turn in [-1,1]:
#             ndir = (dir+turn) % 4
#             state = (result + 1, cut, ny, nx, ndir)
#             if state not in visited:
#                 visited.add(state)
#                 heapq.heappush(q, (result + 1, cut, now_y,now_x, ndir))
#
#
#     return -1
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n,k = map(int,input().split())
#     arr = [list(input())for _ in range(n)]
#     visited = set()
#
#     start_y,start_x = 0,0
#     end_y, end_x = 0, 0
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 'X':
#                 start_y, start_x = i,j
#             if arr[i][j] == 'Y':
#                 end_y, end_x = i,j
#
#     real_result = cut_tree(0,0, start_y, start_x,0)
#     print(f'#{tc} {real_result}')



## 버전_2. 방문 딕셔너리로 구현
# 위의 버전보다는 빠름, 이건 통과한 코드임
# 위와 다른점은 큐에 넣기전 비교를 통해 더 짧은 경로의 경우만 추가했다는 거임
# --> 위의 버전은 그냥 같은 방식으로 간 적만 없으면 추가하는거고, 아래코드는 같은 좌표+같은 방향 일때 더 적은 조작수일때만 추가되게 함

# import heapq
#
# # 델타
# delta = [(-1,0),(0,1),(1,0),(0,-1)]
#
# # 총 조작수, 나무 벤 횟수, 좌표 yx, 방향
# def cut_tree(total,now_cut,start_y,start_x,dir):
#     global n, k, arr, visit_dict
#
#     q = [(total,now_cut,start_y,start_x,dir)]
#
#     # bfs로 풀기 -> 큐 쓰기
#     while q:
#         # 전체 이동
#         result, cut ,now_y,now_x,dir = heapq.heappop(q)
#
#         # 도착지에 도착하면 끝내기
#         if arr[now_y][now_x] == 'Y':
#             return result
#
#         # 직진 시 코드
#         dy,dx = delta[dir]
#         ny,nx = now_y+dy, now_x+dx
#         if 0 <= ny < n and 0 <= nx < n:
#             ncut = cut + 1 if arr[ny][nx] == 'T' else cut
#             key = (ny, nx, dir)
#             # visited을 딕셔너리로하여 현재좌표와 방향을 키값으로 두고 총 조작수를 벨유값으로 넣음
#             # 그래서 같은 키값인데 벨윤값인 총 조작수가 이번게 더 작으면 이번거로 바꾸로 큐에 넣음
#             if ncut <= k and (key not in visit_dict or visit_dict[key] > result+1):
#                 visit_dict[key] = result+1
#                 heapq.heappush(q, (result+1, ncut, ny, nx, dir))
#
#         # 오른쪽 왼쪽 회전 시 (이건 이동아니고 현재 위치에서 방향만 돌린거임,고객 돌린거임)
#         # 회전한 방향으로 해서 나머지 정보들중 조작수만 1을 올리고 나머지는 그대로 다시 큐에 넣기
#         for turn in [-1,1]:
#             # 현재 방향에서 회전 시 4방향중 한쪽으로 돌아가도록, 언제나 델타의 범위인 0~3안의 숫자가 나오도록
#             ndir = (dir+turn) % 4
#             key = (now_y,now_x, ndir)
#             # 위와 같음
#             if key not in visit_dict or visit_dict[key] > result+1:
#                 visit_dict[key] = result+1
#                 heapq.heappush(q, (result + 1, cut, now_y,now_x, ndir))
#
#
#     return -1
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n,k = map(int,input().split())
#     arr = [list(input())for _ in range(n)]
#     # 방문 딕셔너리
#     visit_dict = {}
#
#     start_y,start_x = 0,0
#     end_y, end_x = 0, 0
#     # 도착지와 출발지 좌표 구하기 위한 2차배열 순회
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 'X':
#                 start_y, start_x = i,j
#             if arr[i][j] == 'Y':
#                 end_y, end_x = i,j
#
#     real_result = cut_tree(0,0, start_y, start_x,0)
#     print(f'#{tc} {real_result}')



## 버전_3. for문 막돌려서 풀기

# 하나의 좌표에서 4개의 방향으로 가는 방법에서 각 방향에서 가장 적은 조작수로 가야하니까 한의 좌표->4방향->최소조작수를 배열로 만들어
# for문을 돌려서 계속해서 최소 조작수로만 업데이트가 되도록한다.

import heapq

delta = [(-1,0),(0,1),(1,0),(0,-1)]

def cut_tree(total,now_cut,start_y,start_x,start_dir):
    global arr,n,k,visit

    q = [(total,now_cut,start_y,start_x,start_dir)]

    while q:
        result, now_cut, now_y, now_x, dir = heapq.heappop(q)

        if arr[now_y][now_x] == 'Y':
            return result

        next_y, next_x = now_y + delta[dir][0], now_x + delta[dir][1]
        if 0 <= next_y < n and 0 <= next_x < n:
            ncut = now_cut + 1 if arr[next_y][next_x] == 'T' else now_cut
        # 해당 좌표에서 해당 방향의 이전 조작수와 비교해서 더 작으면 그걸로 진행시킴
             if ncut <= k and visit[next_y][next_x][ncut][dir] > result+1:

                visit[next_y][next_x][ncut][dir] = result+1
                heapq.heappush(q,(result+1, ncut, next_y, next_x, dir))

        for turn in [-1,1]:
            ndir = (dir + turn) % 4
            if visit[now_y][now_x][now_cut][ndir] > result+1:
                visit[now_y][now_x][now_cut][ndir] = result+1
                heapq.heappush(q,(result+1, now_cut, now_y, now_x, ndir))


t = int(input())

for tc in range(1,1+t):
    n,k = map(int,input().split())
    arr = [list(input())for _ in range(n)]

    # 이건 그냥 2차배열
    # visit = [[0]*n for _ in range(n)]

    # 각 좌표 -> 4방향에서 -> 총 조작수(최소로)
    # 이건 한 좌표당 4개의 리스트가 있는 상황 -> (1,1)에 4개의 공간가 있음(상, 하, 좌, 우)
    # visit = [[[False]*4] * n for _ in range(n)]
    # 이건 나무 베는 횟수를 고려하지 않은 것
    # visit = [[[float('inf') for _ in range(4)]for _ in range(n)] for _ in range(n)]

    # 나무 베는 횟수까지 고려한 배열
    visit = [[[[float('inf') for _ in range(4)] for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]

    start_y,start_x = 0,0
    end_y, end_x = 0, 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 'X':
                start_y, start_x = i,j
            if arr[i][j] == 'Y':
                end_y, end_x = i,j

    real_result = cut_tree(0,0, start_y, start_x,0)
    print(f'#{tc} {real_result}')