import sys
sys.stdin = open("../../../IM/input.txt")


# n*n의 배열에 각 칸에 파리가 있다
# m*m사이즈의 파리채가 있다
# 최대한 많은 파리를 죽이자

def fly(nn,mm,map_fly):

    max_pari = -1

    for i in range(nn-mm+1):
        for j in range(nn-mm+1):
            cnt = 0
            for a in range(i,i+mm):
                for b in range(j, j + mm):
                    cnt += map_fly[a][b]

            max_pari = max(max_pari,cnt)

    return max_pari


t = int(input())
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    print(f'#{tc} {fly(n, m, arr)}')