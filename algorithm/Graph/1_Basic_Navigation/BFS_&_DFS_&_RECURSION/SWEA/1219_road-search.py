import sys
sys.stdin = open("input.txt")

## 재귀 스택 큐로 했을 때, 시간 거의 동일&메모리도 동일
# + 인풋을 받아오는 두가지방식 (딕셔너리 & 2차배열)
# + 방문처리 두가지 방식 (set을 이용한 & true false로 확인)


### 재귀로 풀기 (DFS로 풀기)
# 가는 와중에 99가 나오면 멈추고 1을 출력해버림, 끝까지 갔는데 99안나오면 0출력하게
def search(start):
    global visit, res

    for i in dic.get(start,[]):
        # print(i)
        if i == 99:
            res = 1
            return

        if i in visit:
            continue

        visit.add(i)

        search(i)


t = 10
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    # 방문 처리를 true false가 아닌 set을 이용해서 확인하게 하기
    visit = set()
    # print(visit)
    res = 0
    # 갈 수 있는 길을 딕셔너리로 바꿔서 진행
    dic = {}
    for i in range(0,len(arr), 2):
        if dic.get(arr[i]):
            dic[arr[i]].append(arr[i+1])
        else:
            dic[arr[i]] = [arr[i+1]]

    # print(dic)
    search(0)
    print(f'#{tc} {res}')



# ### BFS로 풀기 (q로 풀기)
#
from collections import deque

def q(start):
    global res, way,visit

    li = deque()
    li.append(start)

    while li:
        point = li.popleft()

        for i in way[point]:

            if visit[i]:
                continue

            visit[i] = True
            li.append(i)

            if i == 99:
                res = 1
                return

t = 10
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    visit = [False] * 100
    visit[0] = True
    # 99라는 목적지가 있는 거면 함수 내에서 이 변수를 1로 바꾸게 만들고
    # 99라는 목적지 없이 그냥 함수 끝나면 0이 출력되게함
    res = 0

    # 갈 수 있는 길을 2차배열로
    way = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        way[arr[i]].append(arr[i+1])

    q(0)
    print(f'#{tc} {res}')



### stack으로 풀기
# append pop을 이용해서 푸는 거임

def stack(start):
    global res, way,visit

    li = []
    li.append(start)

    while li:
        point = li.pop()

        for i in way[point]:

            if visit[i]:
                continue
            # print(i, end=" ")
            visit[i] = True
            li.append(i)

            if i == 99:
                res = 1
                return

t = 1
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    visit = [False] * 100
    visit[0] = True
    # 99라는 목적지가 있는 거면 함수 내에서 이 변수를 1로 바꾸게 만들고
    # 99라는 목적지 없이 그냥 함수 끝나면 0이 출력되게함
    res = 0

    # 갈 수 있는 길을 2차배열로
    way = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        way[arr[i]].append(arr[i+1])

    print(way)
    stack(0)
    print(f'#{tc} {res}')



### 유니온파인드로 풀기 ---> 안되는거임!!!!...어떻게 하면 될줄 알았음.....
# 왜냐하면 해당 문제는 단방향 그래프라서 안됨 -> 유니온파인드는 집합을 만들어버리는거라서 방향으로치면 양방향으로서 만들어버리는거임
# 그런데 10개의 테케 중 9개는 맞았던건 그냥 테케가 우연히 (0->34->99)이런식의 방향으로 인풋이 있던거임
# -> 틀린 1개 테케는 (99->0)으로 가는 게 있는데 유니온파인드는 방향 무시하고 하나의 집합으로 넣어버리고 그러면 대표자는 0으로 통일되니까 연결되었다고 답하는거임
# 유니온파인드는 양방향 그래프 문제에서만 사용하도록!

## gpt 설명
# 근데 **유니온 파인드는 집합을 "서로 연결되어 있는 것"**으로 간주해버려.
# 즉, a → b가 있다고 union(a, b)를 하면
# → b → a 도 연결된 것처럼 간주됨 (양방향처럼 처리됨)

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union_find(x, y):
    global res

    ref_x = find(x)
    ref_y = find(y)

    # 주어진 번호의 대표자를 바꿔야 -> 집합끼리 합쳐지는 거니까, 아래처럼 써야함
    if ref_x == 0:
        parents[ref_y] = ref_x
    elif ref_y == 0:
        parents[ref_x] = ref_y
    elif ref_x > ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

    # 0 99로 서로 이어져있을 때, 1을 출력하게 한다.
    if parents[99] == 0:
        res = 1
        return


t = 10
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    parents = [i for i in range(100)]
    res = 0

    for i in range(0, len(arr), 2):
        union_find(arr[i],arr[i+1])

    print(f'#{tc} {res}')