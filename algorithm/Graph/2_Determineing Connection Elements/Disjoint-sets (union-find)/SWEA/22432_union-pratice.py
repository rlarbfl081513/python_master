# 숫자를 연결하는 과정을 거치고
# 중간마다 같은 집합인지 아닌지 확인하는 것을 통해 상태값을 돌려주는

def find_par(x):
    # 계속 움직여서 대표자를 찾도록 해야함
    if x == parents[x]:
        return x

    ref = find_par(parents[x])

    return ref


def union(x, y):
    # 대표자가 같은지 아닌지 확인
    ref_x = find_par(x)
    ref_y = find_par(y)

    # 대표자가 같으면 그냥 리턴
    if ref_x == ref_y:
        return

    # 대표자가 다르면, 그냥 부모가 큰 쪽으로 가게 만들기
    if ref_x < ref_y:
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x


t = int(input())
for tc in range(1, 1 + t):
    n, q = map(int, input().split())
    parents = [i for i in range(n + 1)]
    result = []
    for i in range(q):
        k, a, b = map(int, input().split())
        if k == 1:
            # 연결시키기
            union(a, b)
        else:  # 같은 그룹인지 아닌지 파악하기
            # 같은 그룹이면 예스
            # 아니면 노를
            if find_par(a) == find_par(b):
                result.append('YES')
            else:
                result.append('NO')

    print(f'#{tc}', *result)


### input
# 1
# 4 5
# 1 1 2
# 1 3 4
# 0 2 4
# 1 2 4
# 0 1 2

### output
#1 NO YES