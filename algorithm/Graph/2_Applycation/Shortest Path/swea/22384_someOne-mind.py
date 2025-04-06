import sys
sys.stdin = open("input.txt")

## 문제
# 시어머니는 상하좌우로만 이동가능
# 가중치 = 피로도
# 시어머니가 가장 덜 피곤하게 오는 수치 구하기
# 2차배열에서 가장 높은 값을 가진 곳으로 도착하는 가중치를 구하는

# 2차배열의 값이 곧 가중치, 처음 시작하는 곳의 가중치를 0으로 바꾸는 거 필요없음.
# 델타 떄문에 갔던 곳 또 가서, 방문처리 필요

import heapq

def dijkstra_mind(start_i,start_j):
    global arr,n

    # 일단 다 무한대로 해서 가장 큰 값으로 바꿔
    distance = [[float('inf')]*n for _ in range(n)]
    distance[start_i][start_j] = arr[start_i][start_j]
    # 가중치, 좌표y, 좌표x
    q = [(arr[start_i][start_j], start_i, start_j)]

    # 방문 처리 안하면 무한에 빠져요..아건 상원이의 기차여행이 아니야 그건 딕셔너리로 가는거잖아
    visit = [[0] * n for _ in range(n)]

    while q:
        dis, now_y, now_x = heapq.heappop(q)

        # 이미 적은 피로도로 갔었으면 안감
        # 이 조건을 통과하면 그때 방문처리하는거임
        if dis > distance[now_y][now_x]:
            continue

        # 이미 갔던 곳 안감
        if visit[now_y][now_x] == 1:
            continue

        # 방문처리
        # 해당 좌표의 가중치는 아래의 델타코드를 통해 계속 최단 가중치로 갱신되는거고
        # 이거는 그냥 똑같은 좌표로 또 델타 안돌리게 하는거임 .. 또 이상하게 이해했네
        visit[now_y][now_x] = 1
        # 적은 피로도로 값 갱신
        distance[now_y][now_x] = dis

        # 델타를 통해 인접한 곳들의 값을 적은 피로도로 바꾸기
        for y, x in [(0,1),(1,0),(0,-1),(-1,0)]:
            next_y, next_x = now_y + y, now_x + x

            # 인덱스 벗어난거 나가리
            if 0 > next_y or n <= next_y or 0 > next_x or n <= next_x:
                continue

            # -1은 벽이라고 문제조건이 있어서 이것도 튕기기
            if arr[next_y][next_x] == -1:
                continue

            # 피로도(가중치) 구하기
            next_dis = dis + arr[next_y][next_x]

            # 이미 더 작은 값으로 갔었다면 이번 좌표 나가리
            if next_dis > distance[next_y][next_x]:
                continue

            # 새롭게 구한 더 작은 피로도로 갱신
            distance[next_y][next_x] = next_dis
            # 리스트에 가중치와 좌표 추가하기
            heapq.heappush(q,(next_dis, next_y, next_x))

    return distance


t = int(input())
for tc in range(1,1+t):
    y,x = map(int,input().split())
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 가장 높은 값을 가진 좌표를 구하기 위한 코드
    # + 쓸데없는 것 함 (다른 방식 시도하다 말았음)
    # (가중치, 좌표y, 좌표x) 튜플 형태의 리스트로 구현하려다가 델타를 써야하는거라 ...안되는거 같아서 그만둠
    dic = {}
    for i in range(n):
        dic[i] = []

    # 기륜 강사님 이사한 위치
    home = 0
    home_i,home_j = 0,0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != -1:
                dic[i].append((j,arr[i][j]))
                if home < arr[i][j]:
                    home = arr[i][j]
                    home_i, home_j = i,j

    # print(home, home_j,home_i)
    result = dijkstra_mind(y,x)
    # print(result)
    print(f'#{tc} {result[home_i][home_j]}')


# 인풋값
#
# 2
# 2 1
# 4
# 3 3 3 0
# 3 -1 8 1
# 0 1 -1 1
# 2 0 0 1
# 0 0
# 5
# 1 -1 2 1 2
# 3 -1 1 -1 1
# 0 2 0 -1 0
# 0 -1 0 -1 0
# 0 0 0 -1 5