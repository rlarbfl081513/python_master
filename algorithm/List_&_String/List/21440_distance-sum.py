# n개의 정수가 들어있는 배열에서 이웃한 m개의 합을 계싼하는 것
# m개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 구하라

t = int(input())
for tc in range(1,1+t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    #
    # i + (i+1) + (i+2)