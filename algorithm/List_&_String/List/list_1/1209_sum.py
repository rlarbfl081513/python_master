import sys
sys.stdin = open("input.txt")

t = 10

for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_num = 0

    # 가로 합
    for i in arr:
        total = sum(i)
        max_num = max(max_num, total)

    # 세로 합
    for j in zip(*arr):
        total = sum(j)
        max_num = max(max_num, total)

    # 좌에서 우하단으로 대각선
    cnt_a = 0
    for z in range(100):
        cnt_a += arr[z][z]

    max_num = max(max_num, cnt_a)

    # 우에서 좌하단으로
    cnt_b = 0
    for x in range(99,-1,-1):
        cnt_b += arr[x][x]

    max_num = max(max_num, cnt_b)

    print(f'#{n} {max_num}')
