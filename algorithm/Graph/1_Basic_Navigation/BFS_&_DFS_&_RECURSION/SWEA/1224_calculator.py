import sys
sys.stdin = open("input.txt")

# 앞에서 푼 문제들이랑 비슷한듯 아닌듯

from collections import deque

def calcul(start):
    global box
    if start == len(arr)-1:
        return

    for i in range(start,len(arr)-1):

        if arr[i] not in ['*','+']:
            box.append(int(arr[i]))
        else:
            a = box.pop()

            if arr[i] == '+':
                box.append(a+int(arr[i+1]))
                calcul(i+1+1)
            else:
                box.append(a * int(arr[i+1]))
                calcul(i + 1+1)


t = 10
for tc in range(1,1+t):
    n = int(input())
    arr = deque(list(input()))

    # 아래처럼 쓰면 문자열내의 모든 ()를 제거할 수 있음
    # for i in range(len(arr)):
    #     if arr[i] in '()':
    #         arr[i] = 10
    # target = 10
    # arr = [x for x in arr if x != target]

    print(arr)
    print(n)
    box = []
    calcul(0)
    print(box)


# 어떻게 후위 표기식으로 바꿀까. 굳이 바꿀필요는 없는 건가


# 아래는 후윞기식 계산 코드
# 큐로 풀기 + eval 사용안하고 -> if문으로 경우에 따른 연산을 각각하게 만듦
from collections import deque

def postfix_cal():
    global q_list,pre_q

    q = change_postfix(pre_q)

    while q:
        some = q.popleft()

        if some not in '+*':
            q_list.append(int(some))
        else:
            b = q_list.pop()
            a = q_list.pop()

            if some == '+':
                q_list.append(a + b)
            elif some == '*':
                q_list.append(a * b)


def change_postfix(li):
# 괄호가 열리고 닫히는걸 알아야함


t = 10
for tc in range(1,1+t):
     n = int(input())
     pre_q = deque(list(input().split()))
     q_list = []
     postfix_cal()