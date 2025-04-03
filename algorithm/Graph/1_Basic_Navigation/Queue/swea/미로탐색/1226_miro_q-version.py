import sys
sys.stdin = open("../input.txt")

# 16*16 행렬의 미로
# 읜색은 길 노랑은 벽
# 0,0에서 부터 만들어지고, 1,1에서 시작 --> 도착점은 13,13 --> 길이 있는지 푸는 문제
# 2 가 출발점이고 3이 도착점


# 큐로 풀기
from collections import deque

def q_miro(start_y,start_x):
    global res

    q = deque([(start_y,start_x)])

    while q:
        now_y, now_x = q.popleft()

        if arr[now_y][now_x] == 3:
            res = 1
            return

        arr[now_y][now_x] = 8

        for y,x in [(0,1),(1,0),(0,-1),(-1,0)]:
            next_y, next_x = now_y+y, now_x+x

            if 0 > next_y or next_y > 15 or 0 > next_x or next_x > 15:
                continue

            if arr[next_y][next_x] == 1 or arr[next_y][next_x] == 8:
                continue

            q.append((next_y,next_x))


t = 10
for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(16)] # 문자열인 숫자를 정수로 바꿔줘야 함수에서 숫자마다 ''안쒸워줘도돼서 편함
    # for row in arr:
    #     print(row)
    res = 0
    q_miro(1,1)
    print(f'#{tc} {res}')
