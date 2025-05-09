import sys
sys.stdin = open("input.txt")

# # 1~5000
# # n개의 버스 노선
# # i번째 버스노선
#

## DAT로 풀기
# for tc in range(1, int(input())+1):
#
#     N = int(input())
#
#     nosun = []
#
#     for _ in range(N):
#         start, end = map(int, input().split())
#         nosun.append((start, end))
#     # print(nosun)
#     # [(1, 3), (2, 5)]
#
#     P = int(input())
#
#     # 버스정류장은 1번부터 5000번까지니까 50001로 포문돌리기
#     dat = [0]*5001
#
#     for start, end in nosun:
#         for i in range(start, end+1):
#             # 지나가는 버스정류장(해당 인덱스)에 1씩 숫자를 올린다
#             dat[i] += 1
#
#     res = []
#
#     for _ in range(P):
#         # p개의 버스 정류장에대해 몇개의 버스노선이 다니는지 인풋으로 바로 받으면서 구하기
#         idx = int(input())
#         # if not num:
#         #     continue
#         res.append(dat[idx])
#
#     print(f'#{tc}', *res)




## 딕셔너리, 해시로 풀기

for tc in range(1,1+int(input())):

    n = int(input())
    dict = {}

    for _ in range(n):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            dict[i] = dict.get(i, 0) + 1

    # print(dict)

    new = []
    p = int(input())
    for _ in range(p):
        k = int(input())
        # 아래처럼 쓰면 딕셔너리안에 키가 k인게 있는지 보려고 모든 키벨류 쌍을 다 도는 중인 -- 너무 비효율적임
        # for key,value in dict.items():
        #     if k == key:
        #         new.append(value)

        # k인게 있으면 넣고 아니면 0넣기
        new.append(dict.get(k,0))
    print(f'#{tc}', *new)
