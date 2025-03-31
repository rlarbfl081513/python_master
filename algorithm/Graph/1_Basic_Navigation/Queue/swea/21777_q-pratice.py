from collections import deque


def qqq(queue, a):
    if a[0] == 'enqueue':
        queue.append(a[1])
    elif a[0] == 'front':
        print(queue[0] if queue else -1)
    elif a[0] == 'rear':
        print(queue[-1] if queue else -1)
    elif a[0] == 'dequeue':
        print(queue.popleft() if queue else -1)
    elif a[0] == 'isEmpty':
        print(1 if not queue else -1)
    elif a[0] == 'size':
        print(len(queue))


n = int(input())
queue = deque()

for _ in range(n):
    qqq(queue, input().split())