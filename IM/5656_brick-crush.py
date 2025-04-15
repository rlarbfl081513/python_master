import sys
sys.stdin = open("input.txt")

# 구슬을 쏘아 벽돌을 꺠트린다
# 구슬은 n번만 가능, w*h 배열로 주어진다
# 0은 빈공간, 그외의 숫자는 벽돌
# 게임규칙
    # 구슬을 좌우로만 이동가능, 항상 맨 위의것만 깨기 가능
    # 벽돌은 1~9로 표현
    # 구슬이 명중한 벽돌은 델타로 (벽돌에 적힌 수 - 1)만큼 제거된다.3이 적혀있으면 델타로 2씩 제거됨
    # 델타로 연속되게 깨지는 와중에 중간에 0으로 빈공간이 있어도 무시하고 그냥 영향범위만큼은 다 제거함,
    # 한번 터트리면 다 연속적으로 난리남 -> 그리고 위에 있는 뱍돌은은 아래로 떨어짐
# 최대한 많은 벽돌을 꺠트리고 남은 벽돌의 수를 세라
from collections import deque

def brick(ball_y,ball_x):
    global n,w,h,arr

    # 한번의 경우마다 리스트를 복사해서 써야함
    # 2차원배열에서는 얕은 복사로 인해 원본이 변함
    # new_arr = arr.copy()
    # 2차원배열을 보호하기위해 완전히 새로운 리스트를 만들기 위한 리스트컴프리핸션
    new_arr = [row[:] for row in arr]
    # 부시면서 가장 많이 부신걸 구하면 되는 거임

    ## 아래처럼 반복되는 거니까 재귀를 하면 될듯 -> 재귀를 구슬의 수만큼 반복되게 하기
    ## 경우의 수 구하고 다시 부시는걸 할떄 재귀호출하면 되는 듯

    # 1. 벽돌 처음 부시기
    # 2. 이어붙이기
    # 떨어트릴수 있는 경우의 수 구하기
        # 다시 벽돌 부시기
        # 이어 붙이기
        # 다시 떨어트릴수 있는 경우의 수 구하기
            # 다시 부시기
            # 다시 붙이기
            # 다시 떨어트릴수 있는 경우의 수 구하기

    ## 코드 구현
    # 1. 벽돌 처음 부시기
    # 현재위치에서 가진 만큼 델타로 퍼트리기 --> 연속적으로 터지게 하기
    q = deque([(ball_y,ball_x)])
    while q:
        new_y,new_x = q.popleft()
        for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
            delta_space = arr[new_y][new_x]
            for i in range(1,delta_space):
                ny,nx = ball_y + y*i, ball_x + x*1
                num = 0
                while 0 <= ny < h and 0 <= nx < w:
                    new_arr[ny][nx] = 0
                    q.append((ny,nx))
                    num += 1
                    # 그냥 깨면서 바로 세서 얼만큼 벽돌을 깼는지 알 수 있도록하는거임
                    # cnt += 1
                    ny += y
                    nx += x
    print('부순다음')
    for row in new_arr:
        print(row)
    # 2. 이어붙이기
    ## 맨아래서 부터 가면서 빈칸 있으면 매꾸기
    # for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        # 현재가 0이고 바로 위가 0이 아닌경우일떄
        # box = []
        while True:
            for i in range(h-1,-1,-1):
                if arr[i][j] == 0:
                    # 0바로위에 0이 아닌 값을 가진 좌표라면, 현재 0인 위치에 위의 값을 넣고, 위의값에는 0을 넣어서 아래로 끌어내린 형태를 취한다
                    if i-1 < h and arr[i-1][j] != 0:
                        arr[i][j] = arr[i - 1][j]
                        arr[i - 1][j] = 0
    print('붙인다음')
    for row in new_arr:
        print(row)




    # 부술떄마다 새로운 경우의 수가 생기니까
    # 구슬의 수만큼 경우의 수를 구하는 경우가 늘어남




t = int(input())
for tc in range(1,1+t):
    n,w,h = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(h)]
    for i in arr:
        print(i)
    # 그럼 일단 초기 상태에서 시작점으로 둘수 있는 경우의 수를 구하자
    start_list = []
    for i in range(w):
        j = 0
        while True:
            if arr[j][i] != 0:
                break
            j += 1
        start_list.append((j,i))

    for start_y,start_x in start_list:
        # brick(start_y,start_x)
        brick(1,0)
    # print(start_list)


    # brick()