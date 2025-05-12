import sys
sys.stdin = open("input.txt")

# 주어지는 숫자를 소인수분해
# 2 3 5 7 11


## for & while문 돌려서 찾기
# for tc in range(1,1+int(input())):
#     num = int(input())
#     # print(num)
#     li = [2,3,5,7,11]
#     box = []
#
#     for i in li:
#         cnt = 0
#         while True:
#             if num % i != 0:
#                 break
#             cnt += 1
#             num = num // i
#         box.append(cnt)
#     print(f'#{tc}',*box)



## dictinoary
# for tc in range(1,1+int(input())):
#     num = int(input())
#
#     dict = {}
#     for i in [2,3,5,7,11]:
#         dict[i] = 0
#     # print(dict)
#
#     for i in dict.keys():
#         cnt = 0
#         while True:
#             if num % i != 0:
#                 break
#             cnt += 1
#             num = num // i
#         dict[i] = cnt
#
#     print(f'#{tc}',*[val for val in dict.values()])
#



# # 리스트컴프리핸션 & 함수화
# def pri_def(key,val):
#     cnt = 0
#     while key % val == 0:
#         cnt += 1
#         key //= val
#     return cnt, key
#
# for tc in range(1,1+int(input())):
#     num = int(input())
#     primes = [2,3,5,7,11]
#     result = []
#     for p in primes:
#         cnt, num = pri_def(num,p)
#         result.append(cnt)
#
#     print(f'#{tc}',*result)


## 재귀적으로 소인수 지수 구하기
    # 매번 나누기 연산을 재귀 호출 내에서 직접 처리하는 방식
    # 1. key가 val로 나누어 떨어진때만 1을 더하고 재귀호출
    # 2. 매번 key//val을 인자로 넘기기 떄문에 함수 내에서 num값이 재귀적으로 줄어든다.
    # 3. 반복 대신 재귀를 이용해 나누기 횟수를 세는것
def pri_def(key,val):
    if key % val != 0:
        return 0
    return 1 + pri_def(key//val,val)

for tc in range(1,1+int(input())):
    num = int(input())
    primes = [2,3,5,7,11]
    result = []
    result = [pri_def(num, p) for p in primes]

    print(f'#{tc}',*result)