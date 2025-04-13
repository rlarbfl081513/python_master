import sys
sys.stdin = open("input.txt")


## bfs 버전

from collections import deque

def miro_bfs(node_y,node_x):
    global arr, visit, res

    q = deque([(node_y,node_x)])
    # print(q)

    while q:
        now_y, now_x = q.popleft()
        # print(now_x, now_y)

        if arr[now_y][now_x] == 3:
            res = 1
            return

        visit[now_y][now_x] = True

        for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
            next_y,next_x = now_y+y, now_x+x

            if 0 > next_x or 16 <= next_x or 0 > next_y or 16 <= next_y:
                continue

            if arr[next_y][next_x] == 1:
                continue

            if visit[next_y][next_x]:
                continue

            # 여기서 appendleft 해버리면 그냥 stack(dfs)랑 똑같은거임
            # 그냥 append를 해야 'bfs'임
            q.appendleft((next_y,next_x))


t=10
for tc in range(1,1+t):
    n = int(input())
    # print(n)
    arr = [list(map(int,list(input()))) for _ in range(16)]
    visit = [[False]*16 for _ in range(16)]
    # for row in arr:
    #     print(row)

    res = 0
    # 델타를 통해서 이동하면서 bfs로 가면서, 간곳 또 안가게 방문처리
    # 우선 시작과 끝의 좌표를 구하고
    start_y,start_x = 0,0
    end_y,end_x = 0,0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                start_y,start_x = i,j
            if arr[i][j] == 3:
                end_y,end_x = i,j

    miro_bfs(start_y,start_x)
    print(f'#{tc} {res}')
