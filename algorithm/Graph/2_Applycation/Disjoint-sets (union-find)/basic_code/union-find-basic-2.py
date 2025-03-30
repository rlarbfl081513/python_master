# 6개의 원소 (1~6)이 존재하는 경우

# # 각 집합을 만들어 주는 함수
# def make_set(n):
#     # 1~n까지의 원소가 있다고 가정 -> 총 n개의 집합을 생성
#     # 각 원소의 부모(!= 대표자)를 자신으로 초기화
#     parents = [i for i in range(N+1)]
#     return parents

# 랭크
def make_set(n):

    parents = [i for i in range(N+1)]
    ranks = [0] * (n+1)

    return parents, ranks



# 원형의 find_set 함수코드 (비효율적)
# def find_set(x):
#     # 자신 ==  부모노드 -> 해당 집합의 대표자다
#     # 이렇게 하면 타고타고 들어가서 최종 찐대표자를 찾을 수 있음
#     if parents[x] == x:
#         return x
#
#     # x의 부모노드를 기준으로 다시 대표자를 검색
#     return find_set(parents[x])
#
#     # 여기서 리턴을 안쓰면 최종적으로 찾은 댚값을 돌려주지 않음 그래서 none이 되버림
#     # find_set(parents[x])

## 경로압축 버전
def find_set(x):

    if parents[x] == x:
        return x

    # 경로 압축 (path compression)
    # x의 부모를 대표자로 변경하자
    parents[x] = find_set(parents[x])

    return parents[x]


# 경로압축 다른 버전 (검증 필요)
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x,y):
    # 집합의 합볍은 늘 대표자가 결정해야한다.
    # 내가 삼성 입사했다고 LG랑 합병하는거에 사인할 수 없듯이

    # 1. 대표자 검색 우선 (유니온은 각 요소의 대표자를 찾아오게함-fimd_set함수에서 진행)
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면??
      # 1번의 과정을 통해 알 수 있음
      # 병합하지 않고 그냥 끝내버림
    if ref_x == ref_y:
        return

    # 2-1. 병합 (서로다른 집합이라면)
    # 문제에 따라 우선되는 집합으로 합친다
    # 아래는 더 작은 노드쪽으로 합치는 버전
        # 디버깅 위한것
        # print(ref_x, type(ref_x))
        # print(ref_y, type(ref_y))
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

    # 2-2. rank가 작은쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_y] = ref_x
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_x] = ref_y
    else:
        # 랭크가 같다면 한쪽으로 병합하고 대표자의 랭크 증가 시켜
        parents[ref_x] = ref_y
        ranks[ref_y] += 1



N = 6
parents,ranks = make_set(N)
print(parents)

union(1,3)
union(2,3)
union(5,6)
print(parents)

# 4,5가 같은 집합인가
# parents[4] == parents[5]는 대표자가 아닌 부모노드를 보는 거임
if find_set(4) == find_set(5):
    print('같은 집합')
else:
    print('다른 집합')