import sys
sys.stdin = open("input.txt")

# 높은곳에서 낮은곳으로 옮기는 방식으로 최고점과 최저점의 간격을 줄이는거임
# 작업을 다하면 가장 높은곳과 낮은곳의 차이가 최대 1이내
# 제한된 횟수만큼 옮기고 회고점과 최저점의 차이를 반환

# 덤프의 횟수
# 상자의 높이


## 와일문 돌리기
# def box_move(num,li):
#     # 횟수를 다 쓸떄까지 돌려
#     cnt = 0
#     while True:
#         if num == 0:
#             li.sort()
#             return li[-1] - li[0]
#
#         # 매번 오름차순으로 바꿔서 하는건가
#         li.sort()
#         li[0] = li[0] + 1
#         li[-1] = li[-1] - 1
#         num -= 1
#
# for tc in range(1,11):
#     n = int(input())
#     arr = list(map(int,input().split()))
#
#     print(f'#{tc}',box_move(n,arr))



## 힙큐로 풀기
    # 기본적으로 힙큐는 최소힙구조니까 최대를 구할때는 음수로 바꿔서
import heapq

def heap_box(num,li):
    for_min = li[:]
    for_max = [-x for x in li] # 최대힙을 구하기위해 음수로 만든거
    heapq.heapify(for_min)
    heapq.heapify(for_max)

    while num > 0:
        # 최소힙 구하기
        new_min = heapq.heappop(for_min) + 1
        heapq.heappush(for_min, new_min)

        # 최대힙 구하기
        new_max = -heapq.heappop(for_max) - 1  # 1을 뺴는 계산을 할때는 양수로 만들어서 계산
        heapq.heappush(for_max, -new_max) # 힙큐에 넣을떄는 다시 음수로 만들어서 넣기
        num -= 1

    return -heapq.heappop(for_max) - heapq.heappop(for_min)


for tc in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc}',heap_box(n,arr))