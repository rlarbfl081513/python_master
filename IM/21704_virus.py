import sys
sys.stdin = open("input.txt")

# p크기만큼 델타로 퍼진다
# n*n의 마을에서 -> 가장 많이 바이러스를 죽이는 경우의 죽인 바이러스 수 출력


t = int(input())
for tc in range(1,1+t):
    n, p = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_virus = -1
    for i in range(n):
        for j in range(n):
            kill_virus = arr[i][j]
            for y,x in [(0,-1),(0,1),(1,0),(-1,0)]:
                for num in range(1,p+1):
                    ny,nx = i+y*num, j+x*num
                    if 0 > ny or n <= ny or 0 > nx or n <= nx:
                        continue
                    kill_virus += arr[ny][nx]

            max_virus = max(max_virus,kill_virus)

    print(f'#{tc} {max_virus}')