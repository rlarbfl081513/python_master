# 문제
# 백준의 1931 meetungRoom과 유사한문제인데 전체 시간에 범위가 정해진 버전

def gym():
    global o,c
    cnt = 0
    open_time = 0
    close_time = 0

    for i in range(len(li)):
        if li[i][0] < o:
            continue

        if li[i][1] > c:
            continue

        if open_time <= li[i][1] and close_time <= li[i][0]:
            # print(li[i])
            cnt += 1
            open_time = li[i][0]
            close_time = li[i][1]

    return cnt

t = int(input())
for tc in range(1,1+t):
    o, c = map(int,input().split())
    n = int(input())
    li = []
    for _ in range(n):
        a,b = map(int,input().split())
        li.append((a,b))
    li.sort(key=lambda x:(x[1],x[0]))  # 닫는 시간이 가장 빠른 팀부터 정렬

    print(f'#{tc} {gym()}')


# 인풋
# 3
# 8 16
# 6
# 11 14
# 10 11
# 7 9
# 10 12
# 15 17
# 15 16
# 8 18
# 6
# 3 4
# 3 5
# 17 20
# 12 14
# 13 16
# 16 17
# 10 16
# 6
# 8 9
# 12 14
# 15 16
# 12 15
# 10 12
# 5 6

# 아웃풋
#1 3
#2 2
#3 3