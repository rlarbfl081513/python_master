import sys
sys.stdin = open("input.txt")
import heapq
from collections import defaultdict
# 누전 차단기는 사각형으로 한개만 있음 위치는 0,0
# 콘센트 I의 위치는  좌표 X,Y로 주어짐
# 사이클이 생기면 안된다


## prim
# (정점1,정점2, 가중치)의 튜플 리스트를 만들기위함
# 재귀를 돌면서 만들고 있는데 사실은 완전한 이중 반복문으로 가능
import sys
import heapq
from collections import defaultdict

sys.stdin = open("input.txt")

# 간선 생성 함수
def make_edges(elec):
    edges = []
    for i in range(len(elec)):
        for j in range(i + 1, len(elec)):
            x1, y1, n1 = elec[i]
            x2, y2, n2 = elec[j]
            weight = abs(x1 - x2) + abs(y1 - y2)
            edges.append((n1, n2, weight))
    return edges

# Prim 알고리즘
def prim(start_node, graph, n):
    pq = [(0, start_node)]
    visited = [False] * (n + 1)
    total_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight

        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_weight, next_node))

    return total_weight

# 입력 처리
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    elec = [(0, 0, 0)]  # 0번: 누전차단기

    for i in range(1, n + 1):
        x, y = map(int, input().split())
        elec.append((x, y, i))

    # 간선 만들기
    edges = make_edges(elec)

    # 인접 리스트로 그래프 구성
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    # Prim 실행
    result = prim(0, graph, n)
    print(f'#{tc} {result}')
