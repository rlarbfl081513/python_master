### 문제
# 순환이 생기는지 아닌지 판단하는 문제

# 이거는 부모노드 리스트를 출력해서 트린지 뭔지를 그려서 하는 문제가 아님, 그냥 각각의 것들 이으면서 같은 집합에 있는 것들끼지 이으려고 할때 워닝을 출력하는 문제

# A ~ E는 각각 간선 없이 각자 있는 상태 -> 연결을 시작하는거임
# 각각 다른 집합일때 연결을 시킬 수 있는거임
# 그런데 이미 같은 집합에 있는 애들끼지 유니온을 시키려고 할때 WARNING을 출력하는 거임

def find(x):
    # x가 집합의 대표자다 -> x와 parents[x]가 같다.
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global result

    # 최상위 부모, 그니까 유니온 할 것들의 대표자를 찾아오는 코드
    ref_x = find(x)
    ref_y = find(y)

    # 유니온을 하고 있는데 최상위 부모가 같다는 것은 같은 집합에 있다는 거니까, 순환회로가 되버린다는거임
    if ref_x == ref_y:
        result = 'WARNING'

    # 아래의 대소구분은 문제에 특별한 조건이 있는 게 아니면 어떻게 해도 상관은 없음
    # 어차피 유니온 할 것들끼리는 똑같이 유니온하는 거니까
    if ref_x > ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    parents = [i for i in range(n)]
    # 기본값을 STABLE로 두고 같은 집합내의 것들끼리 연결하려고 할때 WARNING으로 바꿔서 출력이 되게함
    result = 'STABLE'

    # 행렬로 간선을 그을 것들을 인풋으로 받아오니까.
    # 아래처럼 이중 포문을 통해 이어진 부분을 찾아서 그때 유니온을 하도록함
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i][j] == 0:
                continue
            if arr[i][j] != 0:
                union(i, j)

    print(f'#{tc}', result)


### input
# 2
# 5
# 0 0 0 1 0
# 0 0 1 0 0
# 0 1 0 1 1
# 1 0 1 0 1
# 0 0 1 1 0
# 4
# 0 1 0 0
# 1 0 1 0
# 0 1 0 1
# 0 0 1 0

### output
#1 WARNING
#2 STABLE