# 문제
#  양수와 + - ()를 가지고 식을 만듦
# 괄호를 다 지움 --> 괄호를 적절히 쳐서 최소값을 만들어라
import sys
sys.stdin = open("input.txt")

def cut(start):
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