import sys
sys.stdin = open("input.txt")


import sys
sys.stdin = open("input.txt")

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    if x_root != y_root:
        parents[y_root] = x_root

t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(16)]
    parents = [i for i in range(16 * 16)]

    for x in range(16):
        for y in range(16):
            if arr[x][y] != 1:  # 1은 벽, 0이나 2, 3은 길
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 16 and 0 <= ny < 16 and arr[nx][ny] != 1:
                        a = x * 16 + y
                        b = nx * 16 + ny
                        union(a, b)

    # 출발점 (2)의 위치와 도착점 (3)의 위치 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = i * 16 + j
            if arr[i][j] == 3:
                end = i * 16 + j

    if find_set(start) == find_set(end):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



# 내가 시도했지만 망한 코드
# # 기본 유니온파인드 코드
# def find_set(x):
#     if parents[x] == x:
#         return x
#
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
# # 결함시키는
# def union(x,y):
#     ref_x = find_set(x)
#     ref_y = find_set(y)
#
#     if ref_x == ref_y:  # 사이클 방지
#         return
#
#     # 그냥 일정한 규칙으로 연결하려고 이렇게 쓴거임
#     if ref_x < ref_y:
#         parents[ref_y] = ref_x
#     else:
#         parents[ref_x] = ref_y
#
#
# t = 10
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(16)] # 문자열인 숫자를 정수로 바꿔줘야 함수에서 숫자마다 ''안쒸워줘도돼서 편함
#     # for row in arr:
#     #     print(row)

      # 16 x 16 미로니까 총 노드 수는 256개, 인덱스는 0 ~ 255
#     parents = [[i for i in range(16)]*16]
    # 아래 방식이 맞음
    # parents = [i for i in range(16 * 16)]

#     # print()
#     # print(parents)
#

        # i, j는 그냥 행, 열 인덱스인데 이걸 그대로 find_set(i) 이런 식으로 넣으면 의미가 없음
        # 인접한 칸을 union 해야 하는데, **"인접한 0끼리 연결"**을 안 하고 그냥 행과 열 비교만 하고 있어요
#     # for i in range(16):
#     #     for j in range(16):
#     #         if arr[i][j] == 0:
#     #             if find_set(i) != find_set(j):
                    # 여기서 2와 3은 출발지점/도착지점의 값이지 인덱스가 아님!
                    # 즉, 미로 안에서 값이 2인 위치와 3인 위치의 인덱스를 찾아야 해

#     #                 union(i,j)
#     #
#     # if parents[2] == parents[3]:
#     #     print(f'#{tc}',1)
#     # else:
#     #     print(f'#{tc}',-1)
