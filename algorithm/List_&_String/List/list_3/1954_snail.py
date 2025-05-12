import sys
sys.stdin = open("input.txt")

# 달팽이가 n*n 까지의 숫자가 시계방향으로 이루어지게


for tc in range(1,1+int(input())):
    n = int(input())
    arr = n*n
    snail_way = [[0]*n for _ in range(n)]

    num = 1
    start_y,start_x = 0,0
    snail_way[start_y][start_x] = 1

    # 이거 아닌거 같은데
    while 오른쪽 벽을 만날때까지는 오른쪽으로 계속가:
        new_y,new_x = start_y+1,start_x+1
        snail_way[new_y][new_x] = num + 1


    # 벽 만날떄까지 오른쪽으로 이동
    # 벽을 만나면 아레로 이동
    # 이거 왜 모르겠지.///...뭐더라....


    # while True:
    #
    #     for y,x in [(0,1),(0,-1),(1,0),(-1,0)]:
    #         ny,nx = start_y+y, start_x+x
    #         if ny < 0 or ny >= n or nx < 0 or nx >= n:
    #             continue
    #
    #         if arr[ny][nx] != 0:
    #             continue
    #
    #         # 이동하면서 1씩 올리기
    #         # 일단 조건문으로 때리기



    for row in snail_way:
        print(row)