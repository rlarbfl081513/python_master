import sys
sys.stdin = open("input.txt")


# 출발점 후보를 만들고 -> 각각 출발시켜서 도착 하는지 확인....이 아니라 그냥 2에서 시작해서 어디에 도착하는 지 확인하기

# 그러면 arr[99]에서 어디에 2가 있는지 일단 확인하기

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    # for row in arr:
    #     print(row)

    start_y, start_x = len(arr[0])-1, 0
    for i in range(len(arr)):
        if arr[len(arr[0])-1][i] == 2:
            start_x = i

    # print(start_x)
    # 위, 오, 왼으로만 이동하고 지나가는 자리는 1이 아닌 다른숫자로 채워서 , bfs dfs로 하는 건가...???닌가/...??
    stack = [(start_y,start_x)]
    while True:
        cy,cx = stack.pop()
        arr[cy][cx] = 3

        if cy == 0:
            print(f'#{tc} {cx}')
            break

        for y,x in [(0,1),(0,-1),(-1,0)]:
            ny,nx = cy+y, cx+x
            if ny < 0 or ny >= len(arr[0]) or nx < 0 or nx >= len(arr[0]) or arr[ny][nx] != 1:
                continue
            stack.append((ny,nx))

    for row in arr:
        print(row)