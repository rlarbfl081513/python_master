import sys
sys.stdin = open("input.txt")

## 델타를 이용해서 빙글빙글 돌기
# 달팽이가 n*n 까지의 숫자가 시계방향으로 이루어지게

## 0,0에서 시작해서 안으로 들어가는
# delta = [(0,1),(1,0),(0,-1),(-1,0)]
#
# for tc in range(1,1+int(input())):
#     n = int(input())
#     arr = n*n
#     # 채워나가야할 빈 공간
#     snail_way = [[0]*n for _ in range(n)]
#
#     # for row in snail_way:
#     #     print(row)
#
#     # 첫 시작
#     num = 1
#     # 델타 방향을 위한 변수
#     dr = 0
#     # 출발점
#     start_y,start_x = 0,0
#     snail_way[start_y][start_x] = num
#
#     # 1씩 올라가는 숫자가 n*n이 돼었을떄 멈추게하기
#     while num < arr:
#         # 갱신되는 현재 위치
#         ny,nx = start_y+delta[dr][0], start_x+delta[dr][1]
#         # 올바른 조건일떄 현재위치에 숫자 입력하기
#         if 0 <= ny < n and 0 <= nx < n and snail_way[ny][nx] == 0:
#             num += 1                # 숫자 올리기
#             snail_way[ny][nx] = num # 현재위치에 숫자 쓰기
#             start_y,start_x = ny,nx # 현재위치 갱신하기
#         else:
#             # 코너에서 돌아야할때 0123 인덱스를 반복하게 하기
#             # 이미 델타 리스트는 시계방향으로 돌게해놔서 인덱스 순서대로만 가면 달팽이는 자동으로 시계방향으로 계속 돌게되어있음
#             # 그래서 그냥 방향키만 조절해주면 되는거임
#             dr = (dr + 1) % 4
#
#     for row in snail_way:
#         print(row)



# 안에서 바깥으로 돌도록
for tc in range(1, 1 + int(input())):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    # 짝수일떄 델타순서와 시작점
    if n % 2 == 0:
        delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        y, x = n // 2, n // 2-1  # 중앙에서 시작
    else:
        # 홀수 일때의 델타순서와 시작점
        delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        y, x = n // 2, n // 2

    num = n * n - 1  # 시작점은 먼저 찍고 출발하니까 -1 뺴기
    snail[y][x] = n*n
    step = 1
    dir_idx = 0

    while num >= 1:
        # 안에서 부터 나가게되면 2개의 방향으로 이동한 후에 이동해야할 칸 수가 늘어남
        # 그런 특징을 이용해서 for문을 두번돌리는거고, 늘어나는 칸수를 레인지의 step변수로 넣은거임
        for _ in range(2):  # 같은 step을 두 번 반복
            for _ in range(step):
                y += delta[dir_idx][0]
                x += delta[dir_idx][1]
                if 0 <= y < n and 0 <= x < n:
                    snail[y][x] = num
                    num -= 1
            dir_idx = (dir_idx + 1) % 4  # 방향 전환
        step += 1  # 2방향마다 step 증가

    print(f'#{tc}')
    for row in snail:
        print(*row)

