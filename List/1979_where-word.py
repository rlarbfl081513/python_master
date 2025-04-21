import sys
sys.stdin = open("input.txt")

## 문제
# n*n 크기의 단어퍼즐
# k길이의 단어가 들어갈 수 있는 자리의 수 구해 (단어 수에 딱 맞는 자리에만,칸수를 남겨서 들어가는거 안되고)
# 흰색:1. 검은색:0



# # 가로세로 나눠서 포문 돌려서 찾기
# def word(n,k,metrix):
#     total = 0
#     # 델타로 둘러보면서 현재 자리에서 단어수만큼 되는지 확인하기
#     # 가로세로 나눠서 하나???
#     # 해당 줄에 단어수만큼의 1이 있는지부터 확인하면 좀 더 빠르려나...?/굳이 싶은가 일단해
#
#     ## 가로로만 보는 코드
#     for i in range(n):
#         # print(metrix[i].count(1))
#         # 해당 행에 단어수보다 총 공간이 작을떄 나가리
#         if metrix[i].count(1) < k:
#             continue
#         cnt = 0
#         # 이미 인덱스가 단어 길이가 안나올만큼 커지기전에 차단
#         for j in range(n):
#             # 1씩 더하면서 가다가 0이 나타나면 카운트 리셋하고 다시 카운트,
#             if metrix[i][j] == 0:
#                 if cnt == k:
#                     total += 1
#                 cnt = 0
#             else:
#                 cnt += 1
#
#             if j == n-1 and cnt == k:
#                 total += 1
#
#     # # # 세로로만 보는 거
#     for i in range(n):
#
#         cnt = 0
#         for j in range(n):
#             if metrix[j][i] == 0:
#                 if cnt == k:
#                     total += 1
#                 cnt = 0
#             else:
#                 cnt += 1
#
#             if j == n-1 and cnt == k:
#                 total += 1
#
#     return total
#
#
#
#
# t = int(input())
# for tc in range(1,1+t):
#     N,K = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     print(f'#{tc} {word(N,K,arr)}')



## gpt가 최적화해준 버전
# 두개의 함수 사용
    # 1. 가로세로를 나눠서 계산시키는 함수
    # 2. 단어 수 세는 함수

def count_valid_line(line, k):
    cnt = 0
    total = 0
    # 가로로 돌면서 1이 있으면 카운트 올리기
    for val in line:
        if val == 1:
            cnt += 1
        # 0인데 카운트가 단어길이면 total 1 올리기
        else:
            if cnt == k:
                total += 1
            cnt = 0

    # 마지막 칸이 1로 끝날 경우, else로 들어가지 않아서 total값이 1 올라가지 못하니까
    if cnt == k:
        total += 1
    return total


def word(n, k, matrix):
    total = 0

    # 가로 줄 탐색
    for row in matrix:
        total += count_valid_line(row, k)

    # 세로 줄 탐색 (zip으로 전치)
    for col in zip(*matrix):
        total += count_valid_line(col, k)

    return total


# 테스트 케이스 입력
t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {word(N, K, arr)}')
