import sys
sys.stdin = open("input.txt")


# n개의 0과1로 이뤄진 수열에서 연속한 1의 개수중 최댓값을 구하라

# # 일반적 방식
# for tc in range(1,1+int(input())):
#     n = int(input())
#     arr = input()
#
#     max_one = 0
#     cnt = 0
#
#     for i in arr:
#         if i == '1':
#             cnt += 1
#         # 0이면
#         else:
#             max_one = max(max_one,cnt)
#             cnt = 0
#
#     max_one = max(max_one, cnt)
#
#     print(f'#{tc}',max_one)


# ## gpt의 더 짧은 방식
# for tc in range(1,1+int(input())):
#     n = int(input())
#     arr = input()
#     cc = list(map(len,arr.split('0')))
#
#     # print(arr.split('0'))  # ['', '', '11', '', '111', '']
#     # print(cc)  # [0, 0, 2, 0, 3, 0]
#
#     print(f'#{tc}',max(map(len,arr.split('0'))))


## gpt 슬라이딩 윈도우
for tc in range(1, 1 + int(input())):
    n = int(input())
    arr = input()

    max_len = 0
    left = 0  # 슬라이딩 윈도우의 시작

    while left < n:
        if arr[left] == '0':
            left += 1
            continue

        right = left
        while right < n and arr[right] == '1':
            right += 1

        max_len = max(max_len, right - left)
        left = right  # 창을 다음 위치로 이동

    print(f'#{tc}', max_len)
