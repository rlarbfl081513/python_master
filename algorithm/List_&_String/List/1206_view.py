import sys
sys.stdin = open("input.txt")

# 오른쪽 왼쪽 모두 거리 2이상의 공간이 확보되어야함 -> 조망권이 확보된 새대의수를 출력

t = 10

for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int,input().split()))

    # 양옆으로 2개씩 값을 보고 자신보다 낮은 건물인지 확인 -> 차이를 계산
    # 양끝에서 2개씩 떨어진 마지막부분은 각각 오른쪽 왼쪽만 확인하면된다.
    # 주번 4개중에 가장 큰거를 알고 그게 현재 건물보다 작은지 확인...???너무 비효율인가
    total = 0

    for i in range(n):
        max_num = max(arr[i-2:i] + arr[i+1:i+3])
        if max_num < arr[i]:
            total += arr[i]-max_num

    print(f'#{tc} {total}')