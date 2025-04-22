import sys
sys.stdin = open("input.txt")

# h*w 크기의 출입명단이 있음
# 한 사람당 최대 200회 등장 가능
# 출근 횟수가 가장 많은 사원번호 출력 --> 여러명이면 사원번호가 작은 사람 출력

t = int(input())
for tc in range(1,1+t):
    h,w = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    # print(arr)

    person = [0]*10000001

    for i in range(h):
        for j in range(w):
            person[arr[i][j]] += 1

    max_li = []
    for k in range(len(person)):
        if person[k] > 0:
            # 몇번 출근인지 & 사원번호
            max_li.append((person[k],k))

    # max_li.sort(key=lambda x:x[1])
    max_li.sort()
    print(max_li)
    # print(person)

    max_li = max_li[::-1]
    print(max_li)
    min_per = max_li[0][1]
    for a,b in range(len(max_li)):
        if max_li[0][0] == a:
