import sys

from anaconda_project.internal.conda_api import result

sys.stdin = open("input.txt")

# 크루스칼
# 모든 간선들을 보면서, 가장 작은 가중치의 간선부터 고르자 -> 정렬로 가장 작은 걸 고르자 (힙큐로도 가능)
# 이떄 사이클이 발생하면 패스

# 대표자를 검색
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# 결함시키는
def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:  # 사이클 방지
        return

    # 그냥 일정한 규칙으로 연결하려고 이렇게 쓴거임
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y



v,e = map(int, input().split())
edges = []
for _ in range(e):
    start, end, weight = map(int, input().split())
    # 간선들에 대한 정보를 저장함
    edges.append((start, end, weight))

# 원소 두번째를 기준으로 오름차순하라는 말
edges.sort(key=lambda x:x[2])  # 가중치 기준으로 오름차순 정렬
print(edges) # 가장 작은 가중치부터 정렬된 걸 볼 수 있음
parents = [i for i in range(v)]  # make_set (정점을 기준으로 만든거, 간선이 아니라)

# 작은거부터 고르면서 나아가자
# 언제까지? n-1개를 택할때까지
cnt = 0    # 현재까지 선택한 간선의 수
result = 0 # 가중치의 합

for u,v,w in edges:
    # u와 v가 연결이 안되어있으면 선택
    # == 다른 집합이라면
    if find_set(u) != find_set(v):
        # 아래를 통해 어떤 간선들로 나온 가중치의 총합인지 알 수 있음
        print(u,v,w)

        union(u,v)
        cnt += 1
        result += w

        if cnt == v-1:  # mst 구성이 끝났다는거임
            break

print(result)