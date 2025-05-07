import sys
sys.stdin = open("input.txt")


# n개의 양의 정수, 첫번째부터 n번째까지 주어짐
# 최댓값의 위치와 최솟값의 위치의 차이를 절대갑스로 출력
# 가장 작은 수가 여러개이면 먼저 나오는 위치로 하고 가장 큰수가 여러개면 마지막으로 나오는 위치로 함


t = int(input())
for tc in range(1,1+t):
    n = int(input())
    arr = list(map(int,input().split()))

    # 오름차순으로
    new_li = sorted(arr)
    max_num = new_li[-1]
    min_num = new_li[0]

    max_num = max(i for i in range(n) if arr[i] == max_num) + 1
    min_num = min(i for i in range(n) if arr[i] == min_num) + 1
    # print(max_num,min_num)

    print(f'#{tc}', abs(max_num-min_num))