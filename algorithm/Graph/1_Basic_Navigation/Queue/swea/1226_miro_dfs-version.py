import sys
sys.stdin = open("input.txt")

## 재귀를 이용한 DFS로 풀기

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 (행 기준)
dy = [0, 0, -1, 1]  # 상, 하, 좌, 우 (열 기준)

def dfs_miro(x, y):
    # 도착점에 도달하면 True를 반환
    if (x, y) == (13, 13):
        return True

    # 방문 표시
    visited[x][y] = 1

    # 네 방향으로 탐색
    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]

        # 유효한 범위인지 체크 (16x16 범위 안에서)
        if 0 <= nx < 16 and 0 <= ny < 16:
            # 벽이 아닌 곳이고 아직 방문하지 않았다면
            if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                if dfs_miro(nx, ny):  # 재귀적으로 탐색
                    return True

    return False

# 테스트 케이스
t = 1
for tc in range(1, 1 + t):
    n = int(input())  # 테스트 케이스마다 크기를 입력받음
    arr = [list(map(int, list(input()))) for _ in range(16)]  # 미로 입력 받음

    visited = [[0] * 16 for _ in range(16)]  # 방문 여부를 기록할 배열

    # 출발점인 (1, 1)에서 DFS 탐색 시작
    if dfs_miro(1, 1):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


#### 계속 문제를 잘못 이해하는데 이거는 인접행렬에서 델타를 통해 인접한 곳에 있는 0의 값을 가지는 곳으로만 갈 수 있기에 이렇게 풀면안됨
    # 델타를 통해서 주변을 보면서 가야함
#
# def dfs_miro(start):
#     # 시작점을 기준으로 가게하기
#
#
#     for new_node in arr[start]:
#
#         if visited[new_node]:
#             continue
#
#         if len(arr[new_node]) == 0:
#             continue
#         visited[start] = 1
#         dfs_miro(new_node)
#
#
# t = 1
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [list(map(int,list(input()))) for _ in range(16)] # 문자열인 숫자를 정수로 바꿔줘야 함수에서 숫자마다 ''안쒸워줘도돼서 편함
#     new_arr = [[] for _ in range(16)]
#     visited = [0]*16
#     for i in range(16):
#         for j in range(16):
#             if arr[i][j] == 0:
#                 new_arr[i].append(j)
#
#     print(new_arr)
#     dfs_miro(0)
#     print(visited)
#     if visited[2] == 1 and visited[3] == 1:
#         print(f'#{tc}',1)
#     else:
#         print(f'#{tc}',0)
#     # q_miro(1,1)
#     # print(f'#{tc} {res}')
