import sys
sys.stdin = open("input.txt")

# 아래는 후위표기식 계산 코드
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