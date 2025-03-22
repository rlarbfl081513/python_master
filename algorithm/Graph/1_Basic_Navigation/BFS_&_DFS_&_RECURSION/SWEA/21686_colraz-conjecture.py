import sys
sys.stdin = open("input.txt")

# recursion

def cola(num):
    global cnt

    if num == 1:
        print(f'#{tc} {cnt}')
        return

    if num % 2 == 0:  # 짝수
        cnt += 1
        cola(num // 2)
    else:  # 홀수
        cnt += 1
        cola(num * 3 + 1)

t = int(input())
for tc in range(1,1+t):
    n = int(input())
    cnt = 0
    cola(n)



### 큐 덱으로 풀기

from collections import deque

def cola(num):
    global cnt

    q = deque()
    q.append(num)

    while q:
        number = q.popleft()

        if number == 1:
            print(f'#{tc} {cnt}')
            return

        if number % 2 == 0:  # 짝수
            cnt += 1
            q.append(number // 2)
        else:  # 홀수
            cnt += 1
            q.append(number * 3 + 1)

t = int(input())
for tc in range(1,1+t):
    n = int(input())
    cnt = 0
    cola(n)



### input
# 3
# 6
# 13
# 27

### output
#1 8
#2 9
#3 111