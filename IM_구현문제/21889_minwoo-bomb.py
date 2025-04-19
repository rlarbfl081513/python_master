import sys
sys.stdin = open("input.txt")


# N*M 격자에서 폭탄
# 델타로 터지고 각각 k칸으로 퍼진다, 벽이 있으면 폭탄은 차단된다
# # = 벽 / @ = 폭탄 / _ = 빈칸, 폭발 후에는 %가 됨
# 폭탄이 터진 후 상태를 출력하라

def bomb():
    global n,m,k,arr

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                arr[i][j] = '%'
                # 터트리기
                for y,x in [(0,1),(0,-1),(-1,0),(1,0)]:
                    for k_num in range(1,k+1):
                        ny,nx = i+y*k_num, j+x*k_num

                        if 0 > ny or n <= ny or 0 > nx or m <= nx:
                            break
                        if arr[ny][nx] in '#@':
                            break

                        arr[ny][nx] = '%'



t = int(input())
for tc in range(1,1+t):
    n,m = map(int,input().split())
    k = int(input())
    arr = [list(input()) for _ in range(n)]
    # for row in arr:
    #     print(row)
    #
    bomb()
    print(f'#{tc}')
    for row in arr:
        print("".join(row))
