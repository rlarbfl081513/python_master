import sys
sys.stdin = open("input.txt")

# 8:40 - 8:51
# 양면의 돌이 있음, 흰색 검음색
# i번째 돌을 사이에 두고 마주보는 j개의 돌을 같은 색이면 뒤집고 아니면 그대로둬
# 두개는 n 돌의 수와 m 뒤집기 횟수
# 돌의 초기 상태
# m줄에 걸쳐, i j 리스트를 줌
# 1을 시작으로함


t = int(input())

for tc in range(1,1+t):
    n,m = map(int, input().split())
    stone = list(map(int,input().split()))
    for i in range(m):
        a,b = map(int,input().split())
        a = a-1
        for j in range(1,b+1):
            if 0 <= a-j < n and 0 <= a+j < n:
                if stone[a-j] == stone[a+j]:
                    stone[a - j] = 1 - stone[a - j]
                    stone[a + j] = 1 - stone[a + j]


    print(f'#{tc}', *stone)