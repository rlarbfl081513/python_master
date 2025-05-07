import sys
sys.stdin = open("input.txt")

# n개의 정수가 들어있는 배열에서 이웃한 m개의 합을 계싼하는 것
# m개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 구하라

## 해당 문제는 슬라이딩 윈도우 방식을 써야함

t = int(input())

for tc in range(1, 1+t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    window_sum = sum(arr[:m])
    max_num = window_sum
    min_num = window_sum

    for i in range(1,n-m+1):
        # 윈도우를 한탄 오른쪽으로 이동, 가장 앞쪽 값은 빼고 오른쪽 값을 더하는거임
        window_sum = window_sum - arr[i-1] + arr[i+m-1]

        # 최소최대 갱신
        max_num = max(max_num,window_sum)
        min_num = min(min_num,window_sum)

    print(f'#{tc}', max_num - min_num)




## 아래의 두방식은 모두 O(n)이라서 입력이 클 경우 느리다.

# 1. 구간의 범위만큼 for문을 돌면서 하나씩 값을 가져와 더하는 방식
# t = int(input())
# for tc in range(1,1+t):
#     n,m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     box = []
#
#     for i in range(n):
#         cnt = 0
#         if i+(m-1) < n:
#             for j in range(m):
#                 cnt += arr[i+j]
#             box.append(cnt)
#     box.sort()
#
#     print(f'#{tc}',box[-1]-box[0])



# 2. 리스트의 구간을 제한해서 바로 sum을 떄리는 방식
# t = int(input())
#
# for tc in range(1,1+t):
#     n,m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     sum_list = []
#
#     # 구간의 합을 구하기위해 필요한 인덱스 범위 제한
#     for i in range(n-m+1):
#         # 구간을 정해 sum 떄리기
#         a = sum(arr[i:i+m])
#         print(i,i+m,a)
#         sum_list.append(a)
#
#     max_num = max(sum_list)
#     min_num = min(sum_list)
#     print(f'#{tc}', max_num-min_num)
#     print()


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int,input().split()))

    max_num = max(arr)
    min_num = min(arr)

    print(f'#{tc}', max_num-min_num)