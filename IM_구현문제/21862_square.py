import sys
sys.stdin = open("input.txt")


# n*n은 게임판
# 최대한의 면적 큰 사각형을 몇개 그릴 수 있는가
# 왼쪽 상단과 오른쪽 하단의 좌표값이 동일해야한다

# 그냥 무조건 현재 죄표에서 +한 값만 넣어서 같으면 그렇게해서 사각형 그리면됨
# 그러면 이렇게 그려서 오름차순하고 가장 뒤에 있는 값의 개수 세면 되는 거임

def game_map(num,li,start_i,start_j):
    global square

    for i in range(start_i,len(arr)):
        for j in range(start_j, len(arr)):
            if arr[start_i][start_j] == arr[i][j]:
                square.append((i-start_i+1)*(j-start_j+1))


t = int(input())

for tc in range(1,1+t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    square = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            game_map(n,arr,i,j)

    square.sort()
    max_square = square.pop()
    cnt = 1
    for i in range(len(square)):
        if square[i] == max_square:
            cnt += 1

    print(f'#{tc} {cnt}')