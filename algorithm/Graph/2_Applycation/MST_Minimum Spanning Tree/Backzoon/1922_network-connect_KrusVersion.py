
def fin_set(x):
    if parents[x] == x:
        return x

    parents[x] = fin_set(parents[x])
    return parents[x]

def union(x,y):
    ref_x = fin_set(x)
    ref_y = fin_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x


n = int(input())
m = int(input())
edge = []

for _ in range(m):
    start,end,weight = map(int,input().split())
    edge.append((start,end,weight))

edge.sort(key=lambda x:x[2])
parents = [i for i in range(n+1)]
cnt = 0
result = 0

for s,e,w in edge:
    if fin_set(s) != fin_set(e):
        union(s,e)
        cnt += 1
        result += w

        if cnt == m:
            break

print(result)