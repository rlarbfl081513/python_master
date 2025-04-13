import sys
sys.stdin = open("input.txt")

## 문제
# 스노우맨은 상하좌우로만 이동가능
# 땅이 있는 곳에서만 좌우로 이동가능, 수직이동 시에는 게이지가 1씩 오르는데, 리밋을 넘으면 안됨
# 땅을 밟으면 게이지는 0으로 초기화, 게임 시작 시 리밋을 정할 수 있음 -> 최소 리밋값을 출력해
# 보석을 먹기위한 최소 리밋을 구하라

# 1은 땅, 0은 빈공간, 출발은 2, 보석은 3
# 이걸 다익스트라로 풀라고함

## 풀이
# swea '누군가의 속마음'코드를 가지고 풀려고함, 델타를 이용하는 문제라서
#

import heapq

def dijkstra_snow(start_i,start_j):
    global arr, n, m, distance

    distance[start_i][start_j] = 0
    # 최대게이지, 현재 수직 게이지, 좌표y ,좌표x
    q = [(0,0, start_i, start_j)]

    while q:

        gaze,dis, now_y, now_x = heapq.heappop(q)

        # 보석에 도착하면 그만해
        if (now_y, now_x) == (ruby_i,ruby_j):
            return gaze

        # 0은 땅이 아닌 공중으로 이때는 수직 이동만 가능함
        if arr[now_y][now_x] == 0:
            delta = [(1, 0), (-1, 0)]
        # 공중이 아니면 델타로 사방으로 이동 가능
        else:
            delta = [(1, 0), (-1, 0),(0, 1), (0, -1)]
            # 근데 땅일때는 수직이동 값을 0으로 초기화해야한다고함 (문제조건)
            dis = 0

        for y,x in delta:
            # 델타 이동
            next_y, next_x = now_y + y, now_x + x

            # 인덱스 범위 벗어나는거 나가리
            if 0 > next_y or n <= next_y or 0 > next_x or m <= next_x:
                continue

            # 수직이동 일때만 수직 게이지 올라가도록
            if x == 0 :
                next_dis = dis + 1
            # 좌우 이동시에는 수직 게이지에 아무 변화 없도록
            else:
                next_dis = 0

            # 최대 수직 이동 값을 갱신
            # max를 써서 마치 최소 수직 이동값이 아닌 가장 큰 값을 구하는 것처럼 보이지만, 아래로 가면
            new_gaze = max(gaze,next_dis)

            # 힙큐를 쓰기때문에 max를 쓴다하더라고 결국은 가장 작은 max gaze값을 먼저 보고 이동하기에
            # 결국에는 가장 작은 값으로 보석에 도착하게 된다.
            # 최대 수직 이동 값보다 큰 값이 들어가있으면, 작은 값으로 갱신해줌
            if new_gaze < distance[next_y][next_x]:
                distance[next_y][next_x] = new_gaze
                heapq.heappush(q,(new_gaze, next_dis, next_y, next_x))


t = int(input())
for tc in range(1,1+t):
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 최소 이동으로 위한 게이지 값 넣기
    distance = [[float('inf')] * m for _ in range(n)]

    # 보석 위치
    ruby = 3
    ruby_i,ruby_j = 0,0

    # 스노우맨 위치
    snow = 2
    snow_i, snow_j = 0, 0

    # 2차배열 돌면서, 보석이랑 눈사람 위치 구하기
    # 동시에 보석이랑 눈사람있던 자리는 1로 땅으로 처리
    for i in range(n):
        for j in range(m):
            if ruby == arr[i][j]:
                ruby_i,ruby_j = i,j
                # 보석부분 땅으로 처리
                arr[i][j] = 1
            if snow == arr[i][j]:
                snow_i, snow_j = i, j
                # 눈사람 부분 땅으로 처리
                arr[i][j] = 1

    # 리턴값으로 받는 최대 게이지 값을 출력
    result = dijkstra_snow(snow_i, snow_j)
    print(f'#{tc} {result}')
    # print(min_way)
    # for row in distance:
    #     print(row)





## gpt와의 대화 전 혼자 해다가 망한 코드

import sys
sys.stdin = open("input.txt")

import heapq

def dijkstra_snow(start_i,start_j):
    global arr,n, m, min_way, distance

    distance = [[float('inf')]*m for _ in range(n)]
    distance[start_i][start_j] = 0
    q = [(0, start_i, start_j)]

    visit = [[0] * m for _ in range(n)]

    while q:
        dis, now_y, now_x = heapq.heappop(q)

        if dis > distance[now_y][now_x]:
            continue

        distance[now_y][now_x] = dis

        if arr[now_y][now_x] == 0:
            delta = [(1, 0), (-1, 0)]
        else:
            delta = [(1, 0), (-1, 0),(0, 1), (0, 1)]
            dis = 0

        for num in range(len(delta)):
            y,x = delta[num][0], delta[num][1]
            next_y, next_x = now_y + y, now_x + x

            if 0 > next_y or n <= next_y or 0 > next_x or m <= next_x:
                continue

            if num == 0 or num == 1:
                next_dis = dis + 1
                min_way = max(min_way,next_dis)

                if next_dis > distance[next_y][next_x]:
                    continue

                distance[next_y][next_x] = next_dis
                heapq.heappush(q,(next_dis, next_y, next_x))
            else:
                dis = 0
                heapq.heappush(q, (dis, next_y, next_x))

t = int(input())
for tc in range(1,1+t):
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    min_way = float('-inf')
    distance = [[float('inf')] * m for _ in range(n)]

    # 보석 위치
    ruby = 3
    ruby_i,ruby_j = 0,0

    # 스노우맨 위치
    snow = 2
    snow_i, snow_j = 0, 0

    for i in range(n):
        for j in range(m):
            if ruby == arr[i][j]:
                ruby_i,ruby_j = i,j
            if snow == arr[i][j]:
                snow_i, snow_j = i, j

    dijkstra_snow(snow_i, snow_j)
    print(min_way)
    for row in distance:
        print(row)
