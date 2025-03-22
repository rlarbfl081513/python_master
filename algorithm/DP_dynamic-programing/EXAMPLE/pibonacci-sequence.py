# dp 기법을 사용한 피보나치 구현
# 메모이제이션은 아님, 재귀를 사용한게 아니니까

# def pibo(start):
#
#     for i in range(2,start):
#         arr.append(arr[i-2]+arr[i-1])
#
# n = 5
# arr = [0,1]
# pibo(n)
# print(arr)



# 재귀 + dp --> 메모이제이션 사용

def pibo(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = pibo(n-1) + pibo(n-2)
    return memo[n]

n = 5
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
pibo(n)
print(memo)