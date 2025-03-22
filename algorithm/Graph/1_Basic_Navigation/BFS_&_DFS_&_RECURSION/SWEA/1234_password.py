import sys
sys.stdin = open("input.txt")

## 문제 설명
# 0-9로 이뤄진 번호 문자열 -> 같은 번호 붙어있는 쌍들을 소거하고 남은 번호를 비번으로 만듦
# 소거하고 또 쌍이 되면 또 소거

## 알게된 것
# 재귀의 종료조건의 중요성을 깨달은 문제 + retur 위치의 중요성
# 종료조건이 없으면 애써 다 만들어놓은 답을 다시 다 원래 상태로 돌려버림
# 아래 최적화 코드 부분에서 알 수 있듯이 return을 어디에 쓰냐에 따라 원하는 상태에서 함수를 멈출 수 있음


# 재귀
def password(num):
    global n

    # 한번 돌면서 연속되는 수 있는지 보기
    # 소거되면서 리스트의 길이는 계속변하니까 레인지의 범위를 매개변수로 넣음
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            num = num[:i] + num[i+2:]
            return password(num)
        # 인덱스의 끝까지 갔다는 거는 연속되는 숫자가 없었다는 거고 그럼 문제의 조건에 맞는 상태가 된거니까 함수를 멈추고 출력하게 해야함
        # 만약 이 아래와 같은 종료 조건이 없으면, 연속되는 수가 나올떄마다 지우고 다시 함수를 호출하는 것을 다 마치고. 조건에 맞는 상태가 되었을때,
        # 중간에 재귀호출을 하느라 끝까지 못한 포문을 다시 다 돌아가면서 다 돌리기에 결국 결과물은 첫 인풋 상태 그대로로 돌아옴
        elif i == len(num)-2:
            return print(f'#{tc} {" ".join(map(str,num))}')

t = 1
for tc in range(1,t+1):
    n,num = map(int, input().split())
    num = list(map(int,str(num)))
    password(num)


# 최적화 버전
# 굳이 종료조건을 포문안에 if문으로 해서 쓰지 않아도됨
# 그냥 포문을 돌려서 if문에 안걸리고 끝나면 함수가 끝나게 하면되는 거임
def password(num):
    # 한번 돌면서 연속되는 수 있는지 보기
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            # num = num[:i] + num[i+2:]
            return password(num[:i] + num[i+2:])
    return num


t = 1
for tc in range(1,t+1):
    # 아래처럼 문자열로 받아와야 num의 맨 앞이 0이어도 0까지 같이 받아옴
    n, num = input().split()
    print(f'#{tc}',password(num))



# 큐로 풀기
# 주어진 리스트를 앞에서 부터 돌면서
# -> 새로운 리스트에 차례차례 넣으면서 이전(새로운 리스트에 들어간것)과 현재(popleft로 뽑은)의 숫자를 비교하는 방식

from collections import deque

def q(num):
    q_list = deque(num)
    stack = []

    while q_list:
        curr = q_list.popleft()

        if len(stack) > 0 and stack[-1] == curr:
            stack.pop()
        else:
            stack.append(curr)

    return stack


for tc in range(1):
    arr = list(input().split())
    print(*q(arr[1]))



# 스택으로 풀기
# 큐로 푸는 거 그냥 뒤집으면 되는 거임

def stack_def(num):
    num = list(num)
    stack = []

    while num:
        curr = num.pop()

        if len(stack) > 0 and stack[-1] == curr:
            stack.pop()
        else:
            stack.append(curr)

    return reversed(stack)


for tc in range(1):
    arr = list(input().split())
    print(*stack_def(arr[1]))