import sys
sys.stdin = open("input.txt")

# 0~9가 적힌 n장의 카드
# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력해, 카드 장수가 같으면 적힌 숫자가 큰 쪽 출력


## 딕셔너리로 풀기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     num = input()
#     number = list(map(int,list("".join(num))))
#
#
#     # 그냥 딕셔너리에 풀어...??
#     dict = {}
#     for i in number:
#         # 해당하는 키값이 없으면 0을 반환하고, 있으면 해당 벨유에 1을 더하는
#         dict[i] = dict.get(i,0) + 1
#
#     max_val = 0
#     max_key = 0
#     for key,value in dict.items():
#         if value > max_val:
#             max_val = value
#             max_key = key
#         elif max_val == value and max_key < key:
#             max_key = key
#
#     print(f'#{tc} {max_key} {max_val}')




## 리스트로 풀기
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     num = list(map(int,input()))
#
#     li = [0]*10
#
#     for i in num:
#         li[i] += 1
#
#     max_val = 0
#     max_key = 0
#
#     for i in range(10):
#         if li[i] > max_val:
#                 max_val = li[i]
#                 max_key = i
#         elif max_val == li[i] and max_key < i:
#             max_key = i
#
#     print(f'#{tc} {max_key} {max_val}')
#


## enumerate
T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input()))
    li = [0] * 10

    for i in arr:
        li[i] += 1

    A = max(li)
    B = max(i for i, v in enumerate(li) if v == A)

    print(f'#{tc} {B} {A}')
