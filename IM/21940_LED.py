import sys
sys.stdin = open("input.txt")

# 0419
# N개의 조명이 있음
# M번 조명 클릭시 M배수의 조명이 꺼지고 켜짐
# 원하는 조명의 패턴이 주어질때 철수가 눌러야하는 조명의 최소 클릭 횟수 구해라
# 켜진조명 1 꺼진거 0
# 첫번째는 1

## 올바른 코드

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    box = [0] * (n + 1)
    cnt = 0
    # 약간 돌맹이 문제 느낌
    # 리스트를 출력하는것이 아닌 기본값이 모두 0일떄 부터 수정하는 횟수를 구하는 문제이기에
    for i in range(1, n + 1):

        k = 1
        # arr와 box의 인덱스 시작점이 다르다.
        # 때문에 아래와 같이 해야 같은 위치에 있는 숫자를 비교할 수 있다.
        if arr[i] != box[i]:
        # 아래처럼 하면안되는게 지금 문제는 최소로 뒤집는 거니까 아래처럼 쓰면 그냥 같아질떄까지 무작정 뒤집으라는 거임
        # if arr[i] != box[i]:
            cnt += 1
            while 0 < i * k < n + 1:
                box[i * k] = 1 - box[i * k]
                k += 1

    print(f'#{tc} {cnt}')






### 자연재해 수준 코드
# def led(start,total_cnt,recursion):
#     global onoff_list, n, arr,min_onoff
#     # 1번을 먼저 키는거 2번을 먼저 키는거로 해서 경우의 수 뭐시기로??
#
#     # 이제 같아질떄까지 온오프하기
#     # print(new)
#     if arr == new:
#         min_onoff = min(min_onoff, total_cnt)
#         return
#
#     if recursion > 2:
#         return
#
#     for i in range(start+1, n + 1):
#         # 조명 클릭 회수
#
#         total_cnt += 1
#         for j in range(1, n + 1):
#             if i * j < n + 1:
#                 new[i * j] = 1 - new[i * j]
#
#             if arr == new:
#                 min_onoff = min(min_onoff, total_cnt)
#                 return
#
#     return led(0,total_cnt,recursion+1)
#
#
#
#
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = [0] + list(map(int,input().split()))
#
#     min_onoff = float('inf')
#     onoff_list = []
#
#     for i in range(1,n+1):
#         # 1번을 처음으로 키는 경우
#         new = [0]*(n+1)
#         for num in range(1, n + 1):
#             if i*num < n+1:
#                 new[i*num] = 1 - new[i*num]
#         cnt = 1
#         led(i,cnt,0)
#
#     print(f'#{tc} {min_onoff}')
#
