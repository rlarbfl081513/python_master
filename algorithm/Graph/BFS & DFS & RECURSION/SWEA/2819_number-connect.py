
# stack : 레벨 7되면 답에만 저장하고 append하지말것 (lv8 등에서 멈추면 dfs 구조상 하나 탐색하고 멈추기때문에)

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def stack_move(i,j):

    q = []
    q.append((i,j,0,[arr[i][j]]))

    while q:
        start_i, start_j,cnt,path = q.pop()
        if cnt == 7:
            continue
        if cnt == 6:
            if path not in new:
                new.append(path)
                print(path)

        for y,x in delta:
            ny,nx = start_i+y, start_j+x
            if 0 <= ny < 4 and 0 <= nx < 4:
                q.append((ny,nx,cnt+1,path+[arr[ny][nx]]))


T = int(input())
for case in range(T):
    arr = [input().split() for _ in range(4)]
    new = []
    # answer = 0
    # answer_set = set()
    for i in range(4):
        for j in range(4):
            stack_move(i,j)
    print(len(new))


# recursion

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def rec_move(i, j, lv, n):
    global path
    if lv == 6:
        if path not in answer_set:
            answer_set.add(path[:])
            global answer
            answer += 1
        return
    for di, dj in delta:
        new_i = i + di
        new_j = j + dj
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
            continue
        path += my_map[new_i][new_j]
        rec_move(new_i, new_j, lv + 1, n)
        path = path[:-1]


T = int(input())
for case in range(T):
    my_map = [input().split() for _ in range(4)]
    answer = 0
    answer_set = set()
    path = ''
    for i in range(4):
        for j in range(4):
            path += my_map[i][j]
            rec_move(i, j, 0, 4)
            path = path[:-1]
    print(f"#{case + 1} {answer}")



# que : 레벨 6에서 7 탐색하면서 답 다저장하고, que에서 팝한애가 레벨 7이면 8을 탐색하겠다는거니 break걸면됨

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

from collections import deque

def stack_move(i,j):

    q = deque()
    q.append((i,j,0,[arr[i][j]]))

    while q:
        start_i, start_j,cnt,path = q.popleft()
        if cnt == 7:
            break
        if cnt == 6:
            if path not in new:
                new.append(path)
                print(path)

        for y,x in delta:
            ny,nx = start_i+y, start_j+x
            if 0 <= ny < 4 and 0 <= nx < 4:
                q.append((ny,nx,cnt+1,path+[arr[ny][nx]]))



T = int(input())
for case in range(T):
    arr = [input().split() for _ in range(4)]
    new = []
    for i in range(4):
        for j in range(4):
            stack_move(i,j)
    print(len(new))


### input
# 1
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 1 1 1

### output
#1 23