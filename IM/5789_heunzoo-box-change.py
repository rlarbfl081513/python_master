import sys
sys.stdin = open("input.txt")


# 7:46 - 7:57
# 1-n까지의 상자를 가지고 있다, 처음에는 모두 0이 적힘
# q회동안 일정범위의 연속한 상자를 동일한 숫자로 변경하려고한다.
# i번째 작업 -> L ~ R상자까지의 값을 i로 변경
# q회동안 위의 작업을 순서대로 한다음 n개의 상자에 적힌 값들을 순서대로 출력

t = int(input())
for tc in range(1,1+t):
    n,q = map(int, input().split())
    arr = [0]*n
    for i in range(1,1+q):
        l,r = map(int,input().split())
        for j in range(l-1,r+1-1):
            arr[j] = i

    print(f'#{tc} {" ".join(list(map(str,arr)))}')