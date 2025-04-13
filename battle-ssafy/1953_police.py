import sys
sys.stdin = open("input.txt")


## bfs
from collections import deque

from Tools.scripts.findlinksto import visit


def police(start_y,start_x):
    global arr
    dy = [-1,1 ,0, 0]
    dx = [0, 0, -1, 1]

    delta = {
        1: [1,1,1,1],
        2: [1,1,0,0],
        3: [0,0,1,1],
        4: [1,0,0,1],
        5: [0,1,0,1],
        6: [0,1,1,0],
        7: [1,0,1,0],
    }
    visit[start_y][start_x] = 1
    q = deque([(start_y,start_x)])

    while q:
        now_y,now_x = q.popleft()
        dirs = delta[arr[now_y][now_x]]

        for i in range(4):

            # 출구가 안려리면 나가리
            if dirs[i] == 0:
                continue

            next_y, next_x = now_y+dy[i],now_x+dx[i]

            if 0 > next_y or n <= next_y or 0 > next_x or m <= next_x:
                continue

            if visit[next_y][next_x]:
                continue

            # 내가 갈 수 있는 곳인지 판단하기
            if arr[next_y][next_x] == 0:
                continue
            # 다음 파이프
            next_pipe = delta[arr[next_y][next_x]]
            # 내가 상하인데 다음이 좌우로 열려있는 곳이면 나가리
            if i % 2 == 0 and next_pipe[i+1] == 0:
                continue
            # 내가 좌우인데 다음이 상하이면 나가리
            if i % 2 == 1 and next_pipe[i-1] == 0:
                continue

            visit[next_y][next_x] = visit[now_y][now_x]+1
            q.append((next_y,next_x))


t = int(input())
for tc in range(1,1+t):
    n,m,r,c,l = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False]*m for _ in range(n)]
    police(r,c)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if 0 < visit[i][j] <= l:
                cnt += 1
    print(f'#{tc} {cnt}')