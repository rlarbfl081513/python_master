import sys
sys.stdin = open("input.txt")


# 14:42

# 블록의 무게가 그 블록의 비용
# 탑을 쌓는데 드는 총 비용 구해 최소화로
# 조건
    # 두개의 탑 만들어
    # m1 m2
    # 두개의 탑은 123 순으로,
    # 두 탑은 중복되는 거 없음
    # 주어지는 모든 블록 다써야함

# def top_bulid():
#     global n,m1,m2,arr
#
#     # 항상 큰게 m1이 되도록
#     if m1 < m2:
#         m1,m2 = m2,m1
#
#     m1_li = []
#     m2_li = []
#
#     total = 0
#
#     # 최대한 가장 큰 값을 아래로 둔다.그리고 그다음 큰거를 두번째로 둔다
#     # arr.sort()           # 오름차순 1 2 3 4 5
#     # arr = [0]+arr[::-1]  # 뒤집기   0 5 4 3 2 1
#     arr.sort(reverse=True) # 오름차순 + 뒤집기 =  5 4 3 2 1
#
#     m1_cnt = 0
#     m2_cnt = 0
#
#     ## 아래처럼하면 주어진 블록의 수가 짝수일떄는 올바르게 작동할 수 없음
#     # 주어진 블록들을 무거운거 부터 차례대로 넣기
#     # for i in range(1,len(arr),2):
#     #     if i < len(arr) and m1_cnt != m1:
#     #         m1_li.append(arr[i])
#     #         m1_cnt += 1
#     #
#     #     if i+1 < len(arr) and m2_cnt != m2:
#     #         m2_li.append(arr[i+1])
#     #         m2_cnt += 1
#
#     idx = 0
#     while idx < len(arr):
#         if m1 > len(m1_li):
#             m1_li.append(arr[idx])
#             idx += 1
#
#         if m2 > len(m2_li) and idx < len(arr):
#             m2_li.append(arr[idx])
#             idx += 1
#     # print(m1_li)
#     # print(m2_li)
#
#     # m1_li = [0] + m1_li
#     # m2_li = [0] + m2_li
#
#     # 가중치 넣어서 총합 구하기
#     for i in range(len(m1_li)):
#         # 각 블록에는 1부터 곱해야하니까 i + 1한 값을 곱해준다.
#         total += m1_li[i] * (i+1)
#     for j in range(len(m2_li)):
#         total += m2_li[j] * (j+1)
#
#     return total
#
#
# t = int(input())
# for tc in range(1,1+t):
#     n,m1,m2 = map(int,input().split())
#     arr = list(map(int,input().split()))
#
#     print(f'#{tc}',top_bulid())



## 굳이 굳이 while문없이 for문만으로 하고 싶다면
# 총 블럭의 수가 짝홀수로 경우를 나눠서 하려고 해도 너무 복잡만해짐
# 그나마 아래 방식으로 하면 그나마 덜 복잡..??
    # 각 탑에 대해 층수를 부여하고 람다로 오름차순해서 정렬하고, 각 블럭을 무거운 거부터해서 곱해주는거임

def gpt_made():
    global n, m1, m2, arr

    # 블록 무게 내림차순
    arr.sort(reverse=True)

    # 두 탑의 층수만큼 인덱스 준비
    total = 0
    layer_info = []

    # 긴 탑이 먼저 (단, 이 순서는 중요하지 않음, 그냥 둘 합이 m1+m2)
    for i in range(m1):
        layer_info.append(('m1', i + 1))  # (탑 이름, 층수)
    for i in range(m2):
        layer_info.append(('m2', i + 1))

    # 층수 기준으로 정렬
    layer_info.sort(key=lambda x: x[1])  # 낮은 층수부터

    for i in range(len(arr)):
        total += arr[i] * layer_info[i][1]  # 무게 * 층수

    return total

t = int(input())
for tc in range(1,1+t):
    n,m1,m2 = map(int,input().split())
    arr = list(map(int,input().split()))

    print(f'#{tc}',gpt_made())