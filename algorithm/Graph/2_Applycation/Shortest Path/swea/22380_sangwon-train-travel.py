import sys
sys.stdin = open("input.txt")


## 문제
# 0번으로 시작해서 끝 노드로 가는 가중치 구하기 (못가면 impoosible 출력하기)
# 연결 여부 판단과 가중치 구하는 문제
# 연결여부는 처음에 모든 가중치를 무한으로 해놓기때문에 함수를 다 돌리고도 끝 노드의 가중치가 무한이면 방문안했다는 거니까

# 다익스트라는 계속해서 해당 노드로 갈 수 있는 최소 가중치를 구하는 거임

import heapq


def dijkstra(start):
    global graph

    # 모든 가중치를 무한으로 만들어놓음, 최소값으로 계속해서 갱신해야하니까
    distances = {node: float('inf') for node in graph}
    # 처음 출발시에는 가중치가 없으니까 0으로 만듦
    distances[start] = 0
    # (가중치, 노드번호)
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # 이건 2차배열로 해서 델타로 움직이는거 아니고 딕셔너리로 하는거니까
        # visite=0,1 방문처리없이 아래코드만으로 방문처리의 기능을 다할 수 있음
        if current_dist > distances[current_node]:
            continue  # 이미 더 짧은 경로로 방문함

        # 딕셔너리를 통해 연결된 곳들 방문하기
        for neighbor, weight in graph[current_node]:
            # 계속해서 가중치 만들기 ( 더하고 더하고...)
            distance = current_dist + weight

            # 지금 값이 더 작은 값으로 방문하는 상황이면 다시 방문하기
            if distance < distances[neighbor]:
                # 가중치 갱신 (더 작은 값으로)
                distances[neighbor] = distance
                # 리스트에 추가하기
                heapq.heappush(queue, (distance, neighbor))

    # 각 노드에 갱신시킨 가중치 딕셔너리 반환값으로
    return distances


t = int(input())
for tc in range(1,1+t):
    n,t = map(int,input().split())
    graph = {}

    # 연결된 노드끼리의 번호와 가중치 딕셔너리 만들기
    for i in range(n):
        graph[i] = []
    for i in range(t):
     # 노드번호, 노드번호, 가중치 순서로 저장하기
        a,b,w = map(int,input().split())
        graph[a].append((b,w))

    result = dijkstra(0)
    # print(result)
    # 끝 노드를 방문했으면 해당 가중치 출력, 방문안했으면(해당 가중치가 inf그대로면) impossble 출력
    if result[n-1] != float('inf'):
        print(f'#{tc} {result[n-1]}')
    else:
        print(f'#{tc}', "impossible")




# 인풋값
# 2
# 5 8
# 0 1 6
# 0 2 1
# 0 3 7
# 2 3 2
# 3 1 2
# 1 3 4
# 1 4 1
# 4 3 3
# 4 6
# 0 2 5
# 0 1 7
# 2 1 4
# 3 0 2
# 3 2 9
# 3 1 5