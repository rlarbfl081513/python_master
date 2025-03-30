import heapq

def prim(w,s):
    pq = [(w,s)]
    visited = [0]*(v+1)
    min_weight = 0

    while pq:
        weight, start = heapq.heappop(pq)

        if visited[start]:
            continue

        visited[start] = 1
        min_weight += weight

        # 2차배열 탐색 방식 1. start에 해당하는 행을 가져와서 보는 방식
        # for next_node,wei in enumerate(graph[start]):
        #     if wei == 0:
        #         continue
        #
        #     if visited[next_node]:
        #         continue

        # 2차배열 탐색 방식 2. 2차배열 그래프를 돌면서 보는 방식
        for next_node in range(v+1):
            if graph[start][next_node] == 0:
                continue

            if visited[next_node]:
                continue

            heapq.heappush(pq,(graph[start][next_node],next_node))

    return min_weight

t = int(input())
v,e = map(int,input().split())
result = 0

graph = [[0]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
# print(graph)
print(prim(0,1))