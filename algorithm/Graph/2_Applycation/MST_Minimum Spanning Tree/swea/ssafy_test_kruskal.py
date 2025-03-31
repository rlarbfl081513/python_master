import sys
sys.stdin = open("input.txt")
# 누전 차단기는 사각형으로 한개만 있음 위치는 0,0
# 콘센트 I의 위치는  좌표 X,Y로 주어짐
# 사이클이 생기면 안된다


## 크루스칼
# 간선과 가중치를 계산해서 크루스칼로 풀수 있도록하는거임
# (정점1,정점2, 가중치)의 튜플 리스트를 만들기위함
def for_node(node_x,node_y,now_node_num,start,cnt):
    global krus

    if start == len(elec):
        return

    for next_ele in range(start, len(elec)):
        next_x, next_y,node_num = elec[next_ele][0], elec[next_ele][1], elec[next_ele][2]

        if now_node_num == node_num:
            continue

        a = node_x - next_x
        b = node_y - next_y

        if a < 0:
            a = a*(-1)
        if b < 0:
            b = b * (-1)

        weight = a + b
        krus.append((now_node_num,node_num,weight))

    # 다시함수 불러서 경우의수 구하기
    for_node(elec[cnt+1][0], elec[cnt+1][1], elec[cnt+1][2], start+1,cnt+1)


# 작은 가중치부터해서 연결하도록 만드는것, 유니온파인드 구현
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x,y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_y == ref_x:
        return

    if ref_y < ref_x:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    parents = [i for i in range(n+1)]
    elec = [(0,0,0)]  # 여기에 이거 원점하나 추가하면 되는 거였는데!!!!!!!!!!!!!!!
    num = 1
    input_cnt = 0

    # 각 콘센트의 좌표와 번호 붙이기
    for i in range(n):
        input_cnt += 1
        a,b = map(int, input().split())
        elec.append((a,b,input_cnt))
    start = 1
    krus = []
    cnt = 0

    # 크루스칼 구현을 위한 함수 호출
    for_node(elec[cnt][0], elec[cnt][1], elec[cnt][2], 1,cnt)
    # print(krus)
    # 가중치를 기준으로 오름차순
    krus.sort(key=lambda x:x[2])
    # print(krus)
    total = 0

    # 콘센트끼리 연결시키기
    for i in range(len(krus)):
        if find(krus[i][0]) != find(krus[i][1]):
            union(krus[i][0],krus[i][1])
            total += krus[i][2]

    # print(total)

    # 0,0과 가장 가장 가장 가까운 점을 찾아서 거리를 구해
    # way = []
    # for i in range(len(elec)):
    #     a = elec[i][0]
    #     b = elec[i][1]
    #     if elec[i][0] < 0:
    #         a = elec[i][0]*(-1)
    #     if elec[i][1] < 0:
    #         b = elec[i][1]*(-1)
    #     way.append(a+b)

    # way.sort()
    # # print(way)
    # min_way = way[0]
    # # print(min_way)

    # 누전차단기와 가까운거리 + 콘센트간의 최소 거리
    # print(f'#{tc} {total+min_way}')
    print(f'#{tc} {total}')



# 인풋
# 3
# 4
# 5 2
# 8 4
# 8 2
# 10 3
# 3
# -5 0
# -6 -7
# 4 6
# 4
# -8 6
# -7 -1
# -6 7
# -1 3

# 아웃풋
#1 15
#2 23
#3 23