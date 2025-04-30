import sys
sys.stdin = open("input.txt")

# 오른쪽 왼쪽 모두 거리 2이상의 공간이 확보되어야함 -> 조망권이 확보된 새대의수를 출력


## 해당 방식은 비효율적
    # 리스트를 순회하면서 계속 복사(슬라이싱해서 새로운 리스트 만드는 과정)하는 과정이 시간이 많이 들어감
# t = 10
#
# for tc in range(1,1+t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#
#     # 양옆으로 2개씩 값을 보고 자신보다 낮은 건물인지 확인 -> 차이를 계산
#     # 양끝에서 2개씩 떨어진 마지막부분은 각각 오른쪽 왼쪽만 확인하면된다.
#     # 주번 4개중에 가장 큰거를 알고 그게 현재 건물보다 작은지 확인...???너무 비효율인가
#     total = 0
#
#     for i in range(n):
#         max_num = max(arr[i-2:i] + arr[i+1:i+3])
#         if max_num < arr[i]:
#             total += arr[i]-max_num
#
#     print(f'#{tc} {total}')



## 효율적 방식
    # 슬라이싱 없이 직접 인덱스에 접근하는게 좋음
t = 10

for tc in range(1, 1 + t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0

    # 양 끝 두 칸은 비교 대상이 부족하므로 index 2부터 n-3까지
    for i in range(2, n - 2):
        max_side = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > max_side:
            total += arr[i] - max_side

    print(f'#{tc} {total}')
