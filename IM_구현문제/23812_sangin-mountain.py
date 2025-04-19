import sys
sys.stdin = open("input.txt")

# 16:53

# n*n의 맵이 있음
# 델타 방향으로 현재보다 낮은 위치로 가는거임 -> 가장 낮은 곳으로 가는 거임
# 가장 길게 이동한 경우를 구해서 몇칸 이동했는지 구하는 거임

# 높이가 같은건 없음

## 재귀를 이용한 코드
## 자신보다 작은 값으로 갈 길이 있으면 재귀호출하는 거임
def mountain(start_y,start_x,cnt):
    # 델타를 돌면서 자신보다 낮은 위치가 있는 곳으로 이동

    now_val = arr[start_y][start_x]
    min_val = arr[start_y][start_x]
    min_val = min(min_val,now_val)
    min_y,min_x = start_y,start_x

    for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
        ny,nx = start_y+y,start_x+x
        if 0 > ny or n <= ny or 0 > nx or n <= nx:
            continue
        if arr[ny][nx] < min_val:
            min_val = min(min_val, arr[ny][nx])
            min_y, min_x = ny,nx

    if now_val == min_val:
        return cnt
    else:
        return mountain(min_y, min_x,cnt+1)


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split()))for _ in range(n)]
    max_way = 0

    for i in range(n):
        for j in range(n):
            way = mountain(i,j,1)
            max_way = max(max_way,way)
    print(f'#{tc} {max_way}')



import heapq

def mountain(start_y,start_x,val,cnt):
    q = [(val,start_y,start_x,1)]
    new = []

    while q:
        value,next_y,next_x,cnt = heapq.heappop(q)
        # 방금전에 간 길보다 작은 경우에만 움직이기
        new.append(value)


        for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny,nx = next_y+y,next_x+x
            if 0 > ny or n <= ny or 0 > nx or n <= nx:
                continue
            heapq.heappush(q,(arr[ny][nx],ny,nx,cnt+1))




t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split()))for _ in range(n)]
    max_way = 0

    for i in range(n):
        for j in range(n):
            way = mountain(i,j,arr[i][j],1)
            max_way = max(max_way,way)
    print(f'#{tc} {max_way}')