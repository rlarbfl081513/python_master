import sys
sys.stdin = open("input.txt")

# 프림은 특정정점을 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 토드부터 고르자
# 그냥 큐가 아닌 우선순위 큐를 활용하면 굿

import heapq

def prim(start_node):

    pq = [(0,start_node)] # 시작점은 가중치가 0 이다.
    # 언제까지 연결할지는 n개를 모두 연결했을때임
    mst = [0]*v  # visited와 동일
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)
        # 이미 방문한 노드를 뽑았다면 컨티뉴
        if mst[node]:
            continue

        # 이전까지의 bfs는 먼저 본거를 방문하기에 아래의 next_node부분에서 바로 방문처리를 했지만
        # 지금은 주변을 둘러보고 그중 가중치가 작은거를 먼저 방문하는 거라서 둘러본 후 작은걸 뽑는 지금 이자리에서 방문처리를 하는 거임
        mst[node] = 1
        min_weight += weight

        for next_node in range(v):
            # 갈수 없으면패스
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 패스
            if mst[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node],next_node))

    return min_weight



v,e = map(int,input().split())
graph = [[0]*v for _ in range(v)]  # 인접행렬

for _ in range(e):
    start, end, weight = map(int, input().split())
    # 양방향이기에 아래처럼 양방향으로 구현
    graph[start][end] = weight
    graph[end][start] = weight

print(prim(4))  # 출발 정점을 바꾸어도 값이 같음, 계속해서 동일한 최소값을 뽑기 때문이다.
