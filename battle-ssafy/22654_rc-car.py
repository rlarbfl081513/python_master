import sys
sys.stdin = open("input.txt")



from collections import deque

delta = [(-1,0),(0,1),(1,0),(0,-1)]

def cut_tree(start_y,start_x,direc):
    global arr,n,k,visit,res,end_y, end_x


    for i in li:
        if i == 'A':

        elif i == 'L':
        elif i =='R':
    q = deque(li)

    while li:
        i = q.popleft()

        if i == 'A':
            start_y, start_x
        elif i == 'L':
        elif i == 'R':


        if (now_y, now_x) == (end_y, end_x):
            res = 1
            return

        next_y, next_x = now_y + delta[dir][0], now_x + delta[dir][1]
        if 0 <= next_y < n and 0 <= next_x < n:
             if arr[next_y][next_x] == 'G' and visit[next_y][next_x] == 0:
                visit[next_y][next_x] = 1
                q.append((next_y, next_x,dir))

        for turn in [-1,1]:
            ndir = (dir + turn) % 4
            if visit[now_y][now_x] != 0:
                visit[now_y][now_x] = 1
                q.append((now_y, now_x,ndir))


t = int(input())

n = int(input())
arr = [list(input())for _ in range(n)]

m = int(input())

print('#1',end=" " )

for tc in range(m):
    num, li = map(str, input().split())
    num = int(num)
    li = list(li)

    # 나무 베는 횟수까지 고려한 배열
    visit = [[0]*n for _ in range(n)]

    start_y,start_x = 0,0
    end_y, end_x = 0, 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 'X':
                start_y, start_x = i,j
            if arr[i][j] == 'Y':
                arr[i][j] = 'G'
                end_y, end_x = i,j

    cut_tree(start_y, start_x,0)
    print(res, end=" ")