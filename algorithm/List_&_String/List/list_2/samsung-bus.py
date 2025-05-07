import sys
sys.stdin = open("input.txt")

# # 1~5000
# # n개의 버스 노선
# # i번째 버스노선
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#     li = []
#     for i in range(n):
#         a,b = map(int,input().split())
#         for j in range(a,b+1):
#             li.append(j)
#
#     # print(li)
#     new = []
#     p = int(input())
#     for k in range(p):
#         new.append(int(input()))
#     # print(new)
#     box = [0]*p
#     for i in li:
#         if i in new:
#             box[i-1] += 1
#
#     # print(box)
#     print(f'#{tc}',*box)


for tc in range(1, int(input())+1):

    N = int(input())

    nosun = []

    for _ in range(N):
        start, end = map(int, input().split())
        nosun.append((start, end))

    P = int(input())

    dat = [0 for _ in range(5001)]

    for start, end in nosun:
        for i in range(start, end):
            dat[i] += 1

    res = []

    for _ in range(P):
        idx = int(input())
        num = dat[idx]
        if not num:
            continue
        res.append(num)

    print(f'#{tc}', *res)


