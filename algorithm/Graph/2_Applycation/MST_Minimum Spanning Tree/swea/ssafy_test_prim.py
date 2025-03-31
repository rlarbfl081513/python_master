import sys
sys.stdin = open("input.txt")
# 누전 차단기는 사각형으로 한개만 있음 위치는 0,0
# 콘센트 I의 위치는  좌표 X,Y로 주어짐
# 사이클이 생기면 안된다


## prim
# (정점1,정점2, 가중치)의 튜플 리스트를 만들기위함
# 재귀를 돌면서 만들고 있는데 사실은 완전한 이중 반복문으로 가능함
def for_node(node_x,node_y,now_node_num,start,cnt):
    global krus

    if start == len(elec):
        return

    for next_ele in range(start, len(elec)):
        next_x, next_y,node_num = elec[next_ele][0], elec[next_ele][1], elec[next_ele][2]

        if now_node_num == node_num:
            continue

        a = abs(node_x - next_x)
        b = abs(node_y - next_y)

        weight = a + b
        krus.append((now_node_num,node_num,weight))

    # 다시함수 불러서 경우의수 구하기
    for_node(elec[cnt+1][0], elec[cnt+1][1], elec[cnt+1][2], start+1,cnt+1)

# 위의 재귀를 2중반복문으로 구현
def np_recursion(li):
    global krus

    for i in range(len(elec)):
        for j in range(i+1, len(elec)):
            x1,y1,n1 = elec[i]
            x2,y2,n2 = elec[j]
            weight = abs(x1-x2)+abs(y1-y2)
            krus.append((n1,n2,weight))


import heapq

def prim(start_node):
    pq = [(0,start_node)]
    mst = [0]*(n+1)
    min_weight = 0

    while pq:
        e,s = heapq.heappop(pq)
        if mst[s]:
            continue
        mst[s] = 1
        min_weight += e

        for i in range(n+1):
            if graph[s][i] == 0:
                continue
            if mst[i]:
                continue
            heapq.heappush(pq, (graph[s][i],i))
    return min_weight


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    parents = [i for i in range(n+1)]
    elec = [(0,0,0)]  # (정점1,정점2,가중치) 튜플형태의 리스트 생성
    num = 1
    input_cnt = 0

    # 각 콘센트의 좌표와 번호 붙이기
    for i in range(n):
        input_cnt += 1
        a,b = map(int, input().split())
        elec.append((a,b,input_cnt))
    # start = 1
    krus = []
    np_recursion(elec)

    #-----------------------------------------------------위에는 (정점1,정점2,가중치) 튜플형태의 리스트 생성을 위한 코드
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in krus:
        start, end, weight = i[0],i[1],i[2]
        graph[start][end] = weight
        graph[end][start] = weight
    # print(graph)

    prim(0)

    # 누전차단기와 가까운거리 + 콘센트간의 최소 거리
    print(f'#{tc} {prim(0)}')
