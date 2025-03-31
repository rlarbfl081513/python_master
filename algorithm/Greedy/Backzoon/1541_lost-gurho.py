# 문제
#  양수와 + - ()를 가지고 식을 만듦
# 괄호를 다 지움 --> 괄호를 적절히 쳐서 최소값을 만들어라
# import sys
# sys.stdin = open("input.txt")


## 재귀함수로 하는 방법
# ## 아래는 내가 푼 방식인데 백준에서 런타임:인덱스 에러나서.....gpt에게 답을 얻음
# 복잡한 재귀 → IndexError 발생 가능
def cut(start):
    if start == len(val):
        return

    for i in range(start,len(val)):

        if val[i] == '-':
            if '-' not in val[start:i]:
                result.append(val[start:i])
            else:
                return cut(start)

            if '-' not in val[i+1:len(val)]:
                result.append(val[i+1:len(val)])
            else:

                return cut(i+1)

def sumsum(arr):
    li = []
    for item in arr:
        total = 0
        numbers = item.split('+')
        total += sum(map(int,numbers))
        li.append(total)

    real_total = int(li[0])
    for num in li[1:]:
        real_total -= int(num)

    return real_total

val = input()
# val = input()
# result = 55 - 50 + 40  이렇게 숫자랑 연산자랑 띄어쓰기가 있어야 연산된 값이 출렫됨 55-50+40이렇게 붙어있으면 안됨

result = []
# 작은 값을 만들어야하니까 더하기를 먼저하게하고 그다음에 뺴기를 진행하게??
# -를 기준으로 분리하고 계산한다음에 -> -를 진행하게
cut(0)
sumsum(result)
print(sumsum(result))



### 위에 코드 버그 수정 버전
# 아래 함수가 문제였음
def cut(start):
    if start >= len(val):
        return

    for i in range(start, len(val)):
        if val[i] == '-':
            result.append(val[start:i])
            if i + 1 < len(val):
                return cut(i + 1)
            else:
                return

    # 마지막 '-' 이후 or '-'가 아예 없을 때
    result.append(val[start:])


def sumsum(arr):
    li = []
    for item in arr:
        numbers = item.split('+')
        li.append(sum(map(int, numbers)))

    real_total = li[0]
    for num in li[1:]:
        real_total -= num

    return real_total


val = input()  # ex: 55-50+40

result = []
cut(0)
print(sumsum(result))





# ## 연산자에 따라 분리해서 하는 방식
# gpt가 준 답, 백준이 인정한 답
# def sumsum(arr):
#     li = []
#     # +로 묶이 것들을 연산하다.
#     for item in arr:
#         numbers = item.split('+')
#         li.append(sum(map(int, numbers)))
#
#     # 최소값을 구하기위해서는 제일 앞에의 리스트 값을 두고 계속해서 뒤의 값들로 빼기를 진행한다.
#     real_total = li[0]
#     for num in li[1:]:
#         real_total -= num
#
#     return real_total
#
# val = input()  # 입력: 55-50+40
# # -를 기준으로 쪼갠다
# parts = val.split('-')  # ['55', '50+40']
# print(sumsum(parts))    # 55 - (50 + 40) = -35
