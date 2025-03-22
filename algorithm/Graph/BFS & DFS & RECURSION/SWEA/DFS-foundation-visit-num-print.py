### 스택으로 탐색하기

def stack_way(start):
    stack_box = []
    stack_box.append(start)

    while stack_box:

        num = stack_box.pop()
        print(num, end=" ")

        for i in double_list[num]:
            if visit[i]:
                continue
            visit[i] = 1
            stack_box.append(i)

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    visit = [0]*n
    ## 2차배열로 좌표값 받기
    double_list = [[] for _ in range(n)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                double_list[i].append(j)

    # 재귀함수와 같은 경로로 출력하도록 좌표값의 순서를 뒤집어서, append시 반대순서로 들어가게함
    # 뒤집은 리스트 :  [[4, 3, 2], [], [6, 5], [1], [], [], []]
    # 원래   리스트 : [[2, 3, 4], [], [5, 6], [1], [], [], []]
    for i in double_list:
        i.reverse()
    print(f'#{tc}', end=' ')
    stack_way(0)
    print()


## recursion

def dfs(start):
    # 방문처리를 포문안에서하면 첫 시작이 방문처리 되지 않기에 여기다가 하는게 맞음
    visit[start] = 1

    print(start, end=" ")

    # 작은 노드수를 가진거부터 탐색하도록 sort로 정렬
    li = dic.get(start, [])
    li.sort()

    for i in li:
        if visit[i]:
            continue
        dfs(i)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    # 0부터 시작하는
    #   딕셔너리로 좌표값 받기
    dic = {}
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                if dic.get(i):
                    dic[i].append(j)
                else:
                    dic[i] = [j]
    print(f'#{tc}', end=' ')
    dfs(0)
    print()