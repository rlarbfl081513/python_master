import heapq

def heap_def(node):
    global cnt

    if node < 0:
        return

    if (node-1) // 2 >= 0:
        cnt += arr[(node-1) // 2]
    else:
        return

    heap_def((node-1) // 2)


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    cnt = 0
    new = [0]*n

    heap_def(n-1)
    print(f'#{tc} {cnt}')
    # print(arr)
