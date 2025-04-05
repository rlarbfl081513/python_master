# n개의 수를 처리하면서 8자리 암호를 생성
# 8개의 수를 입력받는다.
# 첫 숫자를 1감소하고 맨 뒤로 보낸다
# 그 다음은 2를 감소하고 뒤로, 그다음은 3을 감소하고 뒤로 --> 계속반복하다가
# 감소할때 0보다 작으면 0으로하고, 프로그램은 종료

# 계속해서 popleft와 append를해서 이동
# 1씩 올라가면서 빼는건 cnt를 증가시키면서 마이너스되게 하기

import sys
sys.stdin = open("input.txt")

from collections import deque

### 단순 반복문으로 풀기
# t = 10
# for tc in range(1,1+t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     q = deque(arr)
#     cnt = 0
#
#     while True:
#         cnt += 1
#         if cnt > 5:
#             cnt = 1
#         num = q.popleft()
#         num = num - cnt
#
#         # 0보다 작을때만이 아니라 0일때도 포함해야함
#         if num <= 0:
#             num = 0
#             q.append(num)
#             break
#         q.append(num)
#
#     print(f'#{tc}',*q)



## 재귀로 풀기
## 오직 재귀로만 풀려고하면 안됨...조건을 통해 멈추게한다고 해도 재귀이기에 결국은 엄청나게 많인 돈다.
## 굳이 재귀를 쓴다면 1-5까지 도는걸 재귀로하고, 0이 나올떄까지 돌리는건 와일문을 통해 구현한다.
def recursion_minus(li, num):

    if num > 5:
        return li

    value = li[0] - num

    if value <= 0:
        value = 0
        li = li[1:] + [value]
        return li

    li = li[1:] + [value]
    return recursion_minus(li, num+1)


t = 1
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int,input().split()))

    while True:
        arr = recursion_minus(arr,1)
        if arr[-1] == 0:
            break

    print(f'#{tc}', *arr)


# ## 재귀..절망편
# # 인풋이 작다면 아래처럼 냅다 재귀돌려서 초과안남
# def recursion_minus(li, num):
#
#     if num > 5:
#         num = 1
#
#     value = li[0] - num
#
#     if value <= 0:
#         value = 0
#         li = li[1:] + [value]
#         return li
#
#     li = li[1:] + [value]
#     return recursion_minus(li, num+1)
#
#
#
# t = 1
# for tc in range(1,1+t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#
#     a = recursion_minus(arr,1)
#
#     print(f'#{tc} {a}')