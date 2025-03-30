
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x


t = int(input())

for tc in range(1,t+1):
    v,e = map(int,input().split())
    arr = []
    for _ in range(e):
        a,b,c = map(int,input().split())
        arr.append((a,b,c))
    parents = [i for i in range(v+1)]

    arr.sort(key=lambda x:x[2])
    cnt = 0
    result = 0

    for a,b,c in arr:
        if find(a) != find(b):
            union(a,b)
            cnt += 1
            result += c
            if cnt == e:
                break

    print(f'#{tc} {result}')