# 6개의 원소 (1~6)이 존재하는 경우

def make_set(n):
    parents = [i for i in range(N+1)]
    return parents


def find_set(x):

    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])

    return parents[x]


def union(x,y):

    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


N = 6
parents,ranks = make_set(N)

if find_set(4) == find_set(5):
    print('같은 집합')
else:
    print('다른 집합')