import sys
sys.stdin = open("input.txt")

# # recursion
# # Top-down 재귀 방식
# # 큰 문제 먼저 호출 → 하위 문제 계속 내려가서 해결
# # ex: pascal(5) → 내부에서 pascal(4) → pascal(3)…
#
# def pascal(start):
#
#     if start == 0:
#         return [1]
#
#     else:
#         pre_list = pascal(start-1)
#
#         return [1] + [pre_list[i] + pre_list[i + 1] for i in range(len(pre_list)-1)] + [1]
#
#
# t = int(input())
# for tc in range(1,1+t):
#     cnt = 0
#     n = int(input())
#     print(f'#{tc}')
#     for i in range(n):
#         print(*pascal(i))
#
#
# # dp (dynamic programing)
# # 반복문으로 작은 문제부터 해결
# # # # bootom-up 방식
# # **바텀업(Bottom-up)**은 "문제 해결 순서 기준"이지,
# # 코드 실행 순서나 출력 방향이 아님!, 작은 값부터 쌓아서 큰 값을 만듦
# # ex: dp[0][0] → dp[1][1] → dp[2][1] ...
# # 이미 구한 **작은 문제(dp[i-1][j-1], dp[i-1][j])**를 이용해서
# # **큰 문제(dp[i][j])**를 구함
# # 배열에 값을 누적하며 아래서 위로
#
# def pascal_triangle(n):
#     dp = [[0]*n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 dp[i][j] = 1
#             else:
#                 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#
#     # 출력
#     for i in range(n):
#         print(' ' * (n - i), end='')  # 예쁘게 정렬용
#         for j in range(i + 1):
#             print(dp[i][j], end=' ')
#         print()
#
# # 예시
# pascal_triangle(5)


# 재귀 없는 Bottom-up 스타일의 DP
# 하지만 여기서 재귀를 쓸때 중복호출을 막으면 그것도 dp임
# def pascal(start):
#     global arr
#
#     if start == 0:
#         arr.append([1])
#         return [1]
#
#     else:
#         pre_list = arr[start-1]
#         result = [1] + [pre_list[i] + pre_list[i + 1] for i in range(len(pre_list) - 1)] + [1]
#         arr.append(result)
#         return result
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n = int(input())
#     arr = []
#     print(f'#{tc}')
#     for i in range(n):
#         print(*pascal(i))


# recursion + dp
# 메모이제이션을 이용한 탑다운 방식
# 작은것들을 해결해서 하는거 같지만. 안의 과정을 보면 pascal(5)를 호출해서 pascal(4)를 호출하기에 탑다운인 거임

def pascal(start):
    global arr,memo

    if start == 0:
        memo[start] = [1]
        return [1]

    if start in memo:
        return memo[start]

    pre_list = pascal(start-1)
    result = [1] + [pre_list[i] + pre_list[i + 1] for i in range(len(pre_list) - 1)] + [1]
    memo[start] = result
    return result


t = int(input())
for tc in range(1,1+t):
    memo = {}
    n = int(input())
    arr = []
    print(f'#{tc}')
    for i in range(n):
        print(*pascal(i))